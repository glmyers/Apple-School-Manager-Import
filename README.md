# Apple School Manager Import
Python script to automate the creation of upload files for Apple School Manager from Veracross exports. Note the Veracross export files should be in CSV format and come from queries utilizing the names below. Note that the students query utilized checks to ensure only students with a school email address are exported. Not all our students have functioning email in our system, but they all have an address assigned. Nonfunctioning addresses are store in the 'Email 2' of their record to avoid bounce list issues. The 'gradesNoEmail' funtion in the 'fieldList.py' file is used in the script to ensure the correct email field from the export is used. This fuction is in this file for ease of editing the grades since it email is activated for some grades during the school year. If your school only uses 'Email 1' you can simply delete all grades leaving an empty list. 
## Veracross export files
The script expects five CSV export files from the Veracross school information system in a folder named "downloads" in the current working directory. The 'renameExports.py' script will move exported CSV files from the user's Downloads into the correct folder in the working directory while also striping off the information appeded to query names when downloading CSV files.  
* VCstudents.csv - (*from an export of a Find Students query 251506 must be edited to use your domain*)
* VCstaff.csv - (*from an export of a Find Staff/Faculty query 251505*)
* VCcourses.csv - (*from an export of a Course list query 251503*)
* VCclasses.csv - (*from an export of a Find Class Permissions query 251502*)
* VCrosters.csv - (*from an export of a Find Class Enrollment Records query 251504*)

The results of the script intended to be in a folder named "uploadASM" in the same folder where the script files are located. The names of the Veracross export files and the locations of both input files and output files is set in the "main" function of the script and is easily edited if needed by the individual user.
## Headers of the files for importing
The file fieldsList.py identifies the field names required in the header row of csv import files for Apple School Manager. This file is used by the script creating the files for importing and must be in the same directory as uploadASM.py when it is run. Running this file itself merely outputs a listing of all the field names to the terminal window. The output of field names does also identify which ones are required by Apple School Manager to have a successful import.
## Creating the files for importing
The file uploadASM.py creates five files required by Apple School Manager from the Veracross export files identified above and looks to place them in a folder named "uploadASM" in the current working directory.
* students.csv
* staff.csv
* courses.csv
* classes.csv
* rosters.csv  

The sixth file required by Apple School Manager, locations.csv, needs to exist in the output destination, uploadsASM, prior to running the script and consists of the Description and Abbreviation fields from Veracross School Levels. This file is created and edited manually due to its small size and static nature. The six files used in the upload to Apple School Manager must have these exact names or they upload will fail.

## ZIP file for the import to Apple School Manager
The six files in the output destination are placed in an archive "ASM_files.zip" in the working directory. This is the file to upload into Apple School Manager. Use the individual output files to check the contents of the ZIP file prior to uploading. 
