#!/usr/bin/env python3
'''Creates the import files for Apple School Manager using an exports from
Veracross. Use Google Sheets to transform the Excel files to CSV to preserve
the UTF-8 encoding of the text. The file fieldsAppleSchoolManager.py containing
the export file field names must be in the same folder as this program.

Import file names are set in the main function and the path of their location
is set using the 'inputs' variable.

Export file names should not be altered since ASM is expecting specific
file names. The path of their location is set using the 'results' variable.

****DO NOT CHANGE THE NAMES OF THE RESULT FILES.****
'''

#Import code desired from the standard library.
import csv
from sys import argv
from pathlib import Path
from getpass import getuser
from collections import defaultdict
#Import the fieldnames for the export files.
from fieldsAppleSchoolManager import studentsFields as fstudents
from fieldsAppleSchoolManager import staffFields as fstaff
from fieldsAppleSchoolManager import coursesFields as fcourses
from fieldsAppleSchoolManager import classesFields as fclasses
from fieldsAppleSchoolManager import rostersFields as frosters

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
            new = defaultdict(dict)
            new['person_id'] = row['Person ID']
            new['person_number'] = ''
            new['first_name'] = row['First Name']
            new['middle_name'] = row['Middle Name']
            new['last_name'] = row['Last Name']
            new['grade_level'] = row['Current Grade']
            new['email_address'] = row['Email 1']
            new['sis_username'] = row['Email 1']
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
            if row['Person ID'] not in staffDict:
                new = defaultdict(dict)
                new['person_id'] = row['Person ID']
                new['person_number'] = ''
                new['first_name'] = row['First Name']
                new['middle_name'] = row['Middle Name']
                new['last_name'] = row['Last Name']
                new['email_address'] = row['Email 1']
                new['sis_username'] = row['Email 1']
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
            # if not (row['Role'] == 'Primary Teacher' or
                    # row['Role'] == "Teacher's Aide"): continue
            if row['CLASS: Internal Class ID'] not in classesDict:
                new = defaultdict(dict)
                new['class_id'] = row['CLASS: Internal Class ID']
                new['class_number'] = row['CLASS: Class ID']
                new['course_id'] = row['CLASS COURSE: Internal Course ID']
                new['instructor_id'] = row['STAFF/FACULTY: Person ID']
                new['location_id'] = divisions[row['School Level']]
                classesDict[row['CLASS: Internal Class ID']] = new
            else:
                count = 1
                while count < 16:
                    count += 1
                    if not (classesDict[row['CLASS: Internal Class ID']]
                            [f'instructor_id_{count}'] == {}):
                        continue
                    else:
                        classesDict[row['CLASS: Internal Class ID']]\
                                [f'instructor_id_{count}'] = \
                                    row['STAFF/FACULTY: Person ID']
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


def main():
    print()
    inputs = Path(f'downloads')
    results = Path('uploads')
    #Locations found in Apple School Manager locations.csv
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
    return


if __name__ == '__main__': main()
