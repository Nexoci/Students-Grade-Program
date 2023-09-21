#Made By: Konnor Kobelka
#Created: Sep 19th
#Purpose: A Mini Student Grade Book
import time
global Grades

student_data = [['Marquise','34','77','63','89'],['Johnathan','89','93','97','88'],['Mary Von Bock','9','33','37','12'],['Gary','77','60','83','59']]
options= [0,1,2,3]
print("Welcome To The Student Gradebook")
def menu():
    done = False
    while not done:
        print("Pick What You Would Like To Do")
        try:
            time.sleep(1)
            choice =int(input("\nGradebook Menu:\n0: Add Student\n1: List Students\n2: Calculate Course Averages\n3: Calculate Student Averages\n4. Exit\nEnter your choice: "))
            menus = dict({0:add_student, 1:list_students, 2:course_average, 3:student_average})
            if choice ==4: done = True
            elif choice in options:
                menus[choice]()
        except:
            print("Not real")
        time.sleep(1)
def list_students():
    for student in student_data:
        print(f"Name: {student[0]}\nEnglish: {student[1]}, Physics: {student[2]}, Chemistry: {student[3]}, Math: {student[4]}")        
def add_student():
    name = input("Enter student name: ")
    course1 = float(input("Enter grade for Course 1: "))
    course2 = float(input("Enter grade for Course 2: "))
    course3 = float(input("Enter grade for Course 3: "))
    course4 = float(input("Enter grade for Course 4: "))
    student_data.append([name, course1, course2, course3, course4])
    print("Student data added successfully.")

def course_average():
    print
    
def student_average():
    print()
menu()
