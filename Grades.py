#Made By: Konnor Kobelka
#Created: Sep 19th
#Purpose: A Mini Student Grade Book
import time
global Grades

student_data = [['Marquise','34','77','63','89'],['Johnathan','89','93','97','88'],['Mary Von Bock','9','33','37','12'],['Gary','77','60','83','59']]
print("Welcome To The Student Gradebook")
def options():
    while True:
        time.sleep(1)
        print("\nGradebook Menu:")
        print("1. Add Student")
        print("2. List Students")
        print("3. Calculate Course Averages")
        print("4. Calculate Student Averages")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice =="5":
            break
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

options()

