#!/usr/bin/env python3
'''Creates the import files for Apple School Manager using CSV exports from
Veracross. The file 'locations.csv' is maintained manually using the School
Level from Veracross with location_id being the abriviation and location_name
being the full name.

The file fieldList.py containing the export file field names must be in the
same folder as this program.

Import file names are set in the main function and the path of their location
is set using the 'inputs' variable.

Export file names should not be altered since ASM is expecting specific
file names. The path of their location is set using the 'results' variable.

****DO NOT CHANGE THE NAMES OF THE RESULT FILES.****

ASM_files.zip containing the six files required is created in "uploadASMZ" from
which it is uploaded to Apple School Manager.

The script rquire 'paramiko' and 'dotenv' be installed in Python (use pip).
'''

# Import code desired from the standard library.
import csv
import paramiko
from dotenv import dotenv_values
from sys import argv
from pathlib import Path
from getpass import getuser
from collections import defaultdict
from datetime import datetime
from shutil import make_archive
from shutil import move
#Function to rename and move Veracross CSV exports.
from renameExports import vcxFiles
#Import the fieldnames for the export files.
from fieldList import studentsFields as fstudents
from fieldList import staffFields as fstaff
from fieldList import coursesFields as fcourses
from fieldList import classesFields as fclasses
from fieldList import rostersFields as frosters
# Domain for school email system
domain = '@tsdch.org'
# List of teachers with role "Other" that actually teach the class.
multiTeacher = ['']


def locationDict(filename):
    #Makes a mapping of division name to location_id.
    allLocations = {}
    with open(filename, 'r') as locationList:
        reader = csv.DictReader(locationList)
        for row in reader:
            allLocations[row['location_name']] = row['location_id']
    return allLocations


def createStudents(inFile, outFile, divisions):
    #Create a CSV export file by processing the existing data files.
    with open(inFile, 'r') as dataIn, open(outFile, 'w') as dataOut:
        reader = csv.DictReader(dataIn)
        writer = csv.DictWriter(dataOut, fieldnames=fstudents(),
                                quoting=csv.QUOTE_ALL)
        #Put the header row of fields at the top of the output file.
        writer.writeheader()
        #Output data to the file for all users.
        for row in reader:
            # Confirm student email is in the school domain
            if domain in row['Email 1']:
                sEmail = row['Email 1']
            elif domain in row['Email 2']:
                sEmail = row['Email 2']
            else:
                continue
            new = defaultdict(dict)
            new['person_id'] = row['Person ID']
            new['person_number'] = ''
            new['first_name'] = row['First Nick Name']
            new['middle_name'] = ''
            new['last_name'] = row['Last Name']
            new['grade_level'] = row['Current Grade']
            new['sis_username'] = sEmail
            new['email_address'] = sEmail
            new['password_policy'] = ''
            new['location_id'] = divisions[row['School Level']]
            writer.writerow(new)
    return


def createStaff(inFile, outFile, divisions):
    #Create a CSV export file by processing the existing data files.
    with open(inFile, 'r') as dataIn, open(outFile, 'w') as dataOut:
        reader = csv.DictReader(dataIn)
        writer = csv.DictWriter(dataOut, fieldnames=fstaff(),
                                quoting=csv.QUOTE_ALL)
        #Put the header row of fields at the top of the output file.
        writer.writeheader()
        #Output data to the file for all users.
        staffDict = {}
        for row in reader:
            # Confirm teacher email is in the school domain
            if domain in row['Email 1']:
                sEmail = row['Email 1']
            elif domain in row['Email 2']:
                sEmail = row['Email 2']
            else:
                continue
            if row['Person ID'] not in staffDict:
                new = defaultdict(dict)
                new['person_id'] = row['Person ID']
                new['person_number'] = ''
                new['first_name'] = row['First Nick Name']
                new['middle_name'] = ''
                new['last_name'] = row['Last Name']
                new['email_address'] = sEmail
                new['sis_username'] = sEmail
                new['location_id'] = divisions[row['School Level']]
                staffDict[row['Person ID']] = new
            else:
                count = 1
                while count < 16:
                    count += 1
                    if not staffDict[row['Person ID']][f'location_id_{count}'] == {}:
                        continue
                    else:
                        staffDict[row['Person ID']][f'location_id_{count}'] = \
                                    divisions[row['School Level']]
                        break
        for ID, Staff in staffDict.items():
            writer.writerow(Staff)
    return


def createCourses(inFile, outFile, divisions):
    #Create a CSV export file by processing the existing data files.
    with open(inFile, 'r') as dataIn, open(outFile, 'w') as dataOut:
        reader = csv.DictReader(dataIn)
        writer = csv.DictWriter(dataOut, fieldnames=fcourses(),
                                quoting=csv.QUOTE_ALL)
        #Put the header row of fields at the top of the output file.
        writer.writeheader()
        #Output data to the file for all users.
        for row in reader:
            new = defaultdict(dict)
            new['course_id'] = row['Internal Course ID']
            new['course_number'] = row['Course ID']
            new['course_name'] = row['Course Name']
            new['location_id'] = row['School Level']
            writer.writerow(new)
    return


def createClasses(inFile, outFile, divisions):
    #Create a CSV export file by processing the existing data files.
    with open(inFile, 'r') as dataIn, open(outFile, 'w') as dataOut:
        reader = csv.DictReader(dataIn)
        writer = csv.DictWriter(dataOut, fieldnames=fclasses(),
                                quoting=csv.QUOTE_ALL)
        #Put the header row of fields at the top of the output file.
        writer.writeheader()
        #Output data to the file for all users.
        classesDict = dict()
        for row in reader:
            # do not include those with role of 'Other'
            if row['Person ID'] not in multiTeacher:
                if row['Role'] == 'Other': continue
            # if not (row['Role'] == 'Primary Teacher' or
                    # row['Role'] == "Teacher's Aide"): continue
            if row['Internal Class ID'] not in classesDict:
                new = defaultdict(dict)
                new['class_id'] = row['Internal Class ID']
                new['class_number'] = row['Class ID']
                new['course_id'] = row['Internal Course ID']
                new['instructor_id'] = row['Person ID']
                new['location_id'] = divisions[row['School Level']]
                classesDict[row['Internal Class ID']] = new
            else:
                if row['Role'] == 'Primary Teacher':
                    newTeacher = classesDict[row['Internal Class ID']]['instructor_id']
                    classesDict[row['Internal Class ID']]['instructor_id'] = row['Person ID']
                else:
                    newTeacher = row['Person ID']
                count = 1
                while count < 16:
                    count += 1
                    if not (classesDict[row['Internal Class ID']]
                            [f'instructor_id_{count}'] == {}):
                        continue
                    else:
                        classesDict[row['Internal Class ID']]\
                                [f'instructor_id_{count}'] = \
                                    row['Person ID']
                        break
        for ID, classes in classesDict.items():
            writer.writerow(classes)
    return


def createRosters(inFile, outFile):
    #Create a CSV export file by processing the existing data files.
    with open(inFile, 'r') as dataIn, open(outFile, 'w') as dataOut:
        reader = csv.DictReader(dataIn)
        writer = csv.DictWriter(dataOut, fieldnames=frosters(),
                                quoting=csv.QUOTE_ALL)
        #Put the header row of fields at the top of the output file.
        writer.writeheader()
        for row in reader:
            new = defaultdict(dict)
            new['roster_id'] = row['Enrollment ID']
            new['class_id'] = row['Internal Class ID']
            new['student_id'] = row['Person ID']
            writer.writerow(new)
    return


def sendFile(inFile):
    host = 'upload.appleschoolcontent.com'
    port = 22
    #The code assumes 'usernameASM' and 'passwordASM' are defined in a '.env' file.
    secrets = dotenv_values('.env')
    with paramiko.Transport((host, port)) as transport:
        username = secrets['usernameASM']
        password = secrets['passwordASM']
        transport.connect(username = username, password = password)
        with paramiko.SFTPClient.from_transport(transport) as sftp:
            path = './dropbox/ASM_files.zip'
            localpath = inFile
            sftp.put(localpath, path, callback=None, confirm=False)
    return


def main():
    vcxFiles()
    print()
    inputs = Path(f'downloads')
    results = Path('uploadASM')
    resultsZ = Path('uploadASMZ')
    #Set Locations for ASM in uploadASM locations.csv
    locations = locationDict(f'{results}/locations.csv')
    #Export files from Veracross in CSV format, UTF-8
    sourceStudents = f'{inputs}/VCstudents.csv'
    sourceStaff = f'{inputs}/VCstaff.csv'
    sourceCourses = f'{inputs}/VCcourses.csv'
    sourceClasses = f'{inputs}/VCclasses.csv'
    sourceRosters = f'{inputs}/VCrosters.csv'
    #CSV files for upload into Apple School Manager
    resultStudents = f'{results}/students.csv'
    resultStaff = f'{results}/staff.csv'
    resultCourses = f'{results}/courses.csv'
    resultClasses = f'{results}/classes.csv'
    resultRosters = f'{results}/rosters.csv'
    #Run functions to create the files
    createStudents(sourceStudents, resultStudents, locations)
    createStaff(sourceStaff, resultStaff, locations)
    createCourses(sourceCourses, resultCourses, locations)
    createClasses(sourceClasses, resultClasses, locations)
    createRosters(sourceRosters, resultRosters)
    print('Files are complete.')
    print()
    make_archive(f'{resultsZ}/ASM_files', 'zip', results)
    print('ZIP file is ready.')
    print()
    #Upload the ZIP file via SFTP to Apple School Manager
    sendFile(f'{resultsZ}/ASM_files.zip')
    print('ZIP file uploaded.')
    print()
    return


if __name__ == '__main__': main()

