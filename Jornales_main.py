from Jornales_Student_Record import Record

import os

student = Record()

while (1) :
    os.system("cls")
    try:
        student.menu()
        choice = int(input("\n\tSelect (1-11): "))
    except ValueError:
        os.system("pause")

    if(choice == 1):
        student.reinitialization()
        studentName = input("Enter new student: ")
        student.addName(studentName)

    if(choice == 2):
        for i in range(len(student.listOfSub)):
            print(i+1,"]",student.listOfSub[i])
        for i in range(3):
            subject = input("Choose subject: ")
            student.addSubject(subject)
        student.subjectSorter()

    if(choice == 3):
        for i in range(3):
            grade = input(f"Input grade for {student.subjects[i]}:")
            student.addGrade(grade)
        student.setGrade()
        student.appendDictionary()

    if(choice == 4):
        student.display()

    if(choice == 5):
        studentName = input("Enter student name: ")
        student.search(studentName)
    
    if(choice == 6):
        studentName = input("Enter student name: ")
        student.update(studentName)

    if(choice == 7):
        studentName = input("Enter student name: ")
        student.delete(studentName)
        
    if(choice == 8):
        student.saveRecord()

    if(choice == 9):
        student.retrieveRecord()

    if(choice == 10):
        while(1):
            print("\t\t\tS O R T\n")
            print("\t\t1. Ascending")
            print("\t\t2. Descending")
            option = int(input("\n\tSelect (1-2): "))
            if option == 1:
                student.ascendingBubbleSort()
                break
            if option == 2:
                student.descendingBubbleSort()
                break
            else:
                print('\n\t\tInvalid Input!')
                os.system('\t\tpause')
                break

    if(choice == 11):
        print('\n\t\tPROGRAM FINISHED\n')
        exit()