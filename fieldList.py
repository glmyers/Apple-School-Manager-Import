#!/usr/bin/env python3
'''Field lists for ASM import and grade level functions. This file must be
in the same folder as the uploadASM.py file for it to work as intended.
Running this alone prints a list of the field lists in the file to the terminal.
'''


def gradesNoEmail(grade):
    emailOff = ['TK','K','1','2','3','4','5','6']
    if grade in emailOff:
        return True
    return False


def schoolLevels():
    schoolsDict = {'Lower School':'LS','Middle School':'MS', 'Upper School':'US', \
    'All School':'AS'}
    return schoolsDict


def gradeLevels():
    gradesDict = {'Grade 12':12, 'Grade 11':11, 'Grade 10':10, 'Grade 9':9, \
    'Grade 8':8, 'Grade 7':7, 'Grade 6':6, 'Grade 5':5, 'Grade 4':4, \
    'Grade 3':3, 'Grade 2':2, 'Grade 1':1, 'TK':'Prekindergarten', \
    'Kindergarten':'Kindergarten'}
    return gradesDict


'''Fields for Apple School Manager script
'''
def locationFields():
    #Required: 'location_id', 'location_name'
    fields = ['location_id', 'location_name']
    return fields


def studentsFields():
    #Required: 'person_id', 'first_name', 'last_name', 'location_id'
    fields = ['person_id', 'person_number',
                'first_name', 'middle_name', 'last_name',
                'grade_level', 'email_address', 'sis_username',
                'password_policy',
                'location_id']
    return fields


def staffFields():
    #Required: 'person_id', 'first_name', 'last_name', 'location_id'
    fields = ['person_id', 'person_number',
                'first_name', 'middle_name', 'last_name',
                'email_address', 'sis_username',
                'location_id', 'location_id_2', 'location_id_3',
                'location_id_4', 'location_id_5', 'location_id_6',
                'location_id_7', 'location_id_8', 'location_id_9',
                'location_id_10', 'location_id_11', 'location_id_12',
                'location_id_13', 'location_id_14', 'location_id_15']
    return fields


def coursesFields():
    #Required: 'course_id', 'location_id'
    fields = ['course_id', 'course_number', 'course_name',
                'location_id']
    return fields


def classesFields():
    #Required: 'class_id', 'course_id', 'location_id'
    fields = ['class_id', 'class_number', 'course_id',
                'instructor_id', 'instructor_id_2', 'instructor_id_3',
                'instructor_id_4', 'instructor_id_5', 'instructor_id_6',
                'instructor_id_7', 'instructor_id_8', 'instructor_id_9',
                'instructor_id_10', 'instructor_id_11', 'instructor_id_12',
                'instructor_id_13', 'instructor_id_14', 'instructor_id_15',
                'location_id']
    return fields


def rostersFields():
    #Required: 'roster_id', 'class_id', 'student_id'
    fields = ['roster_id', 'class_id', 'student_id']
    return fields


'''End of field definitions and beginning of main function that prints the
field lists to the terminal window.
'''
def main():
    #Prints the field list for Apple School Manager to the terminal window one per line.
    print('ASM fields Location File:')
    print("Required: 'location_id', 'location_name'")
    for field in locationFields():
        print(field)
    print()
    print('ASM fields Students File:')
    print("Required: 'person_id', 'first_name', 'last_name', 'location_id'")
    for field in studentsFields():
        print(field)
    print()
    print('ASM fields Staff File:')
    print("Required: 'person_id', 'first_name', 'last_name', 'location_id'")
    for field in staffFields():
        print(field)
    print()
    print('ASM fields Courses File:')
    print("Required: 'course_id', 'location_id'")
    for field in coursesFields():
        print(field)
    print()
    print('ASM fields Classes File:')
    print("Required: 'roster_id', 'course_id', 'location_id'")
    for field in classesFields():
        print(field)
    print()
    print('ASM fields Rosters File:')
    print("Required: 'class_id', 'class_id', 'student_id'")
    for field in rostersFields():
        print(field)
    print()
    return

if __name__ == '__main__': main()
