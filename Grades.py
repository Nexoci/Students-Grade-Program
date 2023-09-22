#Made By: Konnor Kobelka
#Created: Sep 19th
#Purpose: A Mini Student Grade Book
import time
global Grades
#2D Array to store student names and grade.
student_data = [['Marquise','34','77','63','89'],['Johnathan','89','93','97','88'],['Mary Von Bock','9','33','37','12'],['Gary','77','60','83','59']]
#options for the dict
options= [0,1,2,3]
print("Welcome To The Student Gradebook")
#display main menu
def menu():
    done = False
    while not done:
        print("Pick What You Would Like To Do")
        try:
            time.sleep(1)
            #users choice
            choice =int(input("\nGradebook Menu:\n0: Add Student\n1: List Students\n2: Calculate Course Averages\n3: Calculate Student Averages\n4. Exit\nEnter your choice: "))
            #dictionary to make choices instead of 100 if statements
            menus = dict({0:add_student, 1:list_students, 2:course_average, 3:student_average})
            #if statement to exit
            if choice ==4: done = True
            elif choice in options:
                menus[choice]()
        except:
            print("Not real")
        time.sleep(1)
#this is what lists the students and their grades
def list_students():
    for student in student_data:
        print(f"Name: {student[0]}\nEnglish: {student[1]}, Physics: {student[2]}, Chemistry: {student[3]}, Math: {student[4]}")
#what adds a new student of your choice        
def add_student():
    name = input("Enter student name: ")
    course1 = float(input("Enter grade for Course 1: "))
    course2 = float(input("Enter grade for Course 2: "))
    course3 = float(input("Enter grade for Course 3: "))
    course4 = float(input("Enter grade for Course 4: "))
    student_data.append([name, course1, course2, course3, course4])
    print("Student data added successfully.")
#calculate and display the courses average
def course_average():
    courses = ["English", "Physics", "Chemistry", "Math"]
    for s_grade in range(1, 5):
        total_marks = 0
        total_students = len(student_data)
        for student in student_data:
            try:
                grade = float(student[s_grade])
                total_marks += grade
            except ValueError:
                #-1 to make sure that the course names and grades match up
                print(f"Invalid grade for {student[0]} in {courses[s_grade - 1]}.")
        if total_students > 0:
            #calculates the average and displays it
            average = total_marks / total_students
            print(f"The Average Grade For {courses[s_grade - 1]} is: {average:.2f}")
        else: print(f"No valid grades found for {courses[s_grade - 1]}.")           
#calculate and display the individual students average 
def student_average():
    student_name = input("Enter the student's name: ")
    done = False
    for student in student_data:
        if student[0].lower() == student_name.lower():
            #gathers the grade from studend_data and adds it up from index 1-3 
            total_marks = sum([float(grade) for grade in student[1:]])
            #calculates thhe average
            average = total_marks / 4 
            print(f"The average grade for {student_name} is: {average:.2f}")
            done = True          
    if not done:
        print(f"{student_name} not found in the gradebook.")
menu()
