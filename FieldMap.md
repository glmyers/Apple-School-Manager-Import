# Field Mapping
## Locations
Apple School Manager | Veracross - *School Levels*
-------------------------|------------------------
location_id | Abbreviation
location_name | Description
## Students
Apple School Manager | Veracross - *Find Students*
-------------------------|------------------------
person_id | Person ID
person_number | ''
first_name | First Name
middle_name | Middle Name
last_name | Last Name
grade_level | Current Grade
email_address | Email 1
sis_username | Email 1
password_policy | ''
location_id | School Level *lookup* Abbreviation
## Staff
Apple School Manager | Veracross - *Find Staff/Faculty*
-------------------------|------------------------
person_id | Person ID
person_number | ''
first_name | First Name
middle_name | Middle Name
last_name | Last Name
email_address | Email 1
sis_username | Email 1
location_id | School Level *lookup* Abbreviation
## Courses
Apple School Manager | Veracross - *Course List* (must have a section)
-------------------------|------------------------
course_id | Internal Course ID
course_number | Course ID
course_name | Course Name
location_id | School Level
## Classes
Apple School Manager | Veracross - *Find Class Permissions*
-------------------------|------------------------
class_id | CLASS: Internal Class ID
class_number | CLASS: Class ID
course_id | CLASS COURSE: Internal Course ID
instructor_id | STAFF/FACULTY: Person ID
location_id | School Level *lookup* Abbreviation
## Rosters
Apple School Manager | Veracross - *Find Class Enrollment Records*
-------------------------|------------------------
roster_id | Enrollment ID
class_id | Internal Class ID
student_id | Person ID
