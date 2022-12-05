import os
import csv

class Record():

    student_header = ['Name', 'ENGLISH', 'FILIPINO', 'HISTORY', 'MATH', 'SCIENCE', 'Average']
    listOfSub = ['ENGLISH', 'FILIPINO', 'HISTORY', 'MATH', 'SCIENCE']
    
    def __init__(self):
        self.record = []
        self.student = ['None', 0, 0, 0, 0, 0, 0]
        self.grade = [0,0,0,0,0,0,0]
        self.grades = []
        self.subjects = []
    
    @staticmethod
    def menu():
        print("\t\t\tM E N U\n")
        print("\t\t1. Add Student")
        print("\t\t2. Add Subject")
        print("\t\t3. Add Grade")
        print("\t\t4.View/Display All Student Record ")
        print("\t\t5.Search Student Record")
        print("\t\t6.Update Student Record")
        print("\t\t7.Delete Student Record")
        print("\t\t8.Save Student Record to csv file")
        print("\t\t9.Read Student Record from a csv file")
        print("\t\t10.Sort Student by Average (Ascending and Descending Order)")
        print("\t\t11.Quit")

    def reinitialization(self):
        self.listOfSub = ['ENGLISH', 'FILIPINO', 'HISTORY', 'MATH', 'SCIENCE']
        self.student = ['None', 0, 0, 0, 0, 0, 0]
        self.grade = [0,0,0,0,0,0,0]
        self.grades = []
        self.subjects = []

    def addName(self, studentName):
        self.student[0] = studentName

    def addSubject(self, subject):
        self.listOfSub.remove(subject.upper())
        for i in range(len(self.listOfSub)):
            print(i+1,"]",self.listOfSub[i])
        self.subjects.append(subject)

    def subjectSorter(self):
        self.subjects = sorted(self.subjects)

    def addGrade(self, grade):
        self.grades.append(grade)

    def setGrade(self):
        counter = 0
        for i in range (len(self.subjects)):
            if self.subjects[i].upper() in self.student_header:
                self.grade[self.student_header.index(self.subjects[counter].upper())] = self.grades[counter]
                counter += 1
            else: 
                self.grade[i] = 0

    def appendDictionary(self):
        counter = 0
        for i in range(len(self.student_header)):
            if self.grade[i] != 0:
                self.student[self.student_header.index(self.subjects[counter].upper())] = self.grade[i]
                counter += 1
        self.record.append(self.student)

    def display(self):  
        print(f'{self.student_header[0]: <10}{self.student_header[1]: <12}{self.student_header[2]: <14}{self.student_header[3]: <16}{self.student_header[4]: <18}{self.student_header[5]: <20}{self.student_header[6]}')
        for row in self.record:
            print(f'{row[0]: <10}{row[1]: <12}{row[2]: <14}{row[3]: <16}{row[4]: <18}{row[5]: <20}{row[6]}')
        os.system("pause")

    def search(self, studentName):
        for i in range(len(self.record)):
            if studentName in self.record[i]:
                print('NAME:', self.record[i][0])
                print('\nENGLISH:', self.record[i][1])
                print('\nFILIPINO:', self.record[i][2])
                print('\nHISTORY:', self.record[i][3])
                print('\nMATH:', self.record[i][4])
                print('\nSCIENCE:', self.record[i][5])
                print('\nAVERAGE:', self.record[i][6])
                os.system('pause')
        else: 
            print('\nSTUDENT NOT FOUND!')
            os.system('pause')

    def saveRecord(self):
        with open('students.csv', 'w',newline = "") as file:
            w = csv.DictWriter(file, fieldnames=self.student_header)
            w.writeheader()
            writer = csv.writer(file)
            writer.writerows(self.record)

    def retrieveRecord(self):
        with open('students.csv') as file_obj:
            reader_obj = csv.reader(file_obj)
            for row in reader_obj:
                self.record.append(row)
            self.record.pop(0)
        self.display()
    