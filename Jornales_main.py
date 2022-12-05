from Jornales_Student_Record import Record

import os

student = Record()

while (1) :
    os.system("cls")
    try:
        student.menu()
        choice = int(input("Select (1-11):"))
    except ValueError:
        os.system("pause")

    if(choice == 1):
        student.reinitialization()
        studentName = input("Add student: ")
        student.addName(studentName)

    if(choice == 2):
        for i in range(len(student.listOfSub)):
            print(i+1,"]",student.listOfSub[i])
        for i in range(3):
            subject = input("Add subject: ")
            student.addSubject(subject)
        student.subjectSorter()

    if(choice == 3):
        for i in range(3):
            grade = input(f"Add grade for {student.subjects[i]}:")
            student.addGrade(grade)
        student.setGrade()
        student.appendDictionary()

    if(choice == 4):
        student.display()

    if(choice == 5):
        studentName = input("Add student: ")
        student.search(studentName)
        
    if(choice == 8):
        student.saveRecord()

    if(choice == 9):
        student.retrieveRecord()
