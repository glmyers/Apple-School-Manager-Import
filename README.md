# Apple School Manager Import
Python script to automate the creation of upload files for Apple School Manager from Veracross exports. Note the Veracross export files should be in CSV format and come from queries utilizing the names below. 
## Domain and Email
Export files from Veracross need to contain both __Email 1__ and __Email 2__. Not all our students have functioning email in our system, but they all have an address assigned. Nonfunctioning addresses are stored in the __Email 2__ of their record to avoid bounce list issues.
The 'domain' global variable located under the import statements is used to manage which email field is utilized and can function in many ways to meet various needs as shown in these examples:
* __'@tsdch.org'__ checks Email 1 for an address in the "tsdch.org" domain, then Email 2 if Email 1 fails, but skips the person if both fail;
* __'tsdch.org'__ functions as above, but would allow for addresses in subdomains such as "@students.tsdch.org" to be used;
* __'@'__ checks Email 1 for any address, then Email 2 if Email 1 fails, but skips the person if neither contains an address;
* __''__ causes Email 1 to be used regardless of the contents of the field.

## Veracross export files
The script expects five CSV export files from the Veracross school information system in a folder named "downloads" in the current working directory. The 'renameExports.py' script will move exported CSV files from the Downloads in the user's home directory (*if exports are located elsewhere, simply edit the variable __sourceFolder__ in 'renameExports.py'*) into the correct folder in the working directory while also striping off the information appeded to query names when downloading CSV files.   
* VCstudents.csv - (*from an export of a Find Students query 251506*)
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
