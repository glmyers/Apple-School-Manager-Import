# Apple School Manager Import
Python script to automate the creation of upload files for Apple School Manager from Veracross exports. Note the Veracross export files are in Excel format and must be converted to CSV. Do not use Excel to make this conversion because the result would be ASCII encoded rather the desired UTF-8 encoding. Importing the file into a Google spreadsheet allows simple download of the file as CSV with UTF-8 encoding.
## Veracross export files
The script expects five CSV export files from the Veracross school information system in the Downloads folder of a user on a Mac OS computer with the standard drive name of Macintosh HD.   
* VCstudents.csv (*from an export of a Find Students querry*)
* VCstaff.csv (*from an export of a Find Staff/Faculty querry*)
* VCcourses.csv (*from an export of a Course list querry*)
* VCclasses.csv (*from an export of a Find Class Permissions querry*)
* VCrosters.csv (*from an export of a Find Class Enrollment Records querry*)

The results of the script intended to be in a folder named "uploads" in the same folder where the script files are located. The names of the Veracross export files and the locations of both input files and output files is set in the "main" function of the script and is easily edited if needed by the individual user.
## Headers of the files for importing
The file fieldsAppleSchoolManager.py identifies the field names required in the header row of csv import files for Apple School Manager. This file is used by the file creating the files for importing and must be in the same directory as uploadAppleSchoolManager.py when it is run. Runing this file itself merely outputs a listing of all the field names to the terminal window. The output of field names does also identify which ones are required by Apple School Manager to have a successful import.
## Creating the files for importing
The file uploadAppleSchoolManager.py creates five files required by Apple School Manager from the Veracross export files identified above. 
* students.csv 
* staff.csv 
* courses.csv 
* classes.csv 
* rosters.csv  

The sixth file required by Apple School Manager, locations.csv, needs to exist in the output destination, uploads, prior to runing the script. The six files used in the upload to Apple School Manager must have these exact names or they upload will fail.
