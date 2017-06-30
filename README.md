# Apple-School-Manager-Import
Python script to automate the creation of upload files for Apple School Manager from Veracross exports.

The file fieldsAppleSchoolManager.py identifies the field names required in the header row of csv import files for Apple School Manager. Runing this file will output a listing of all the field names an identify which ones are required by Apple School Manager to have a successful import.

The file uploadAppleSchoolManager.py creates five files required by Apple School Manager students.csv, staff.csv, courses.csv, classes.csv, and rosters.csv from the Veracross export files. The sixth file required by Apple School Manager, locations.csv, needs to exist in the output location, uploads, prior to runing the script. 

The script expects five CSV export files from the Veracross school information system; VCstudents.csv, VCstaff.csv, VCcourses.csv, VCclasses.csv, and VCrosters.csv to be in the Downloads folder of a user on a Mac OS computer with the standard drive name of Macintosh HD. The results of the script intended to be in a folder named "uploads" in the same folder where the script files are located. The names of the Veracross export files and the locations of both input files and output files is set in the "main" function of the script and is easily edited if needed by the individual user.