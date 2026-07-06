student={}
import json 
while (True): 
    print("---STUDENT MANAGEMENT SYSTEM---")
    print("1. is for add an student")
    print("2. is for view all students")
    print("3. is for search an individual student")
    #print("4. is for check marks")
    print("5 is for delete an student")
    print("6 is for saving data")
    print("7 is for loading data") 
    print("8 is for exit")
    choice=input("Enter your choice: ")
    if (choice=="1"): 
        name=input("Enter the name of student: ")
        marks=int(input("Enter the marks of student: "))
        student[name]=marks
        print("Student added in Database!")
        print()
    elif(choice=="2"): 
            for name, marks in student.items():
                print(f"{name}:{student[name]}")
                print()

    elif(choice=="3"):
        name=input("Enter the name of student: ")
        if name in student:
            print(f"The name and marks of student are : {name}:{student[name]}")
        
        else: 
            print("student not found!")
            print()
    elif(choice=="5"):
        name = input("Enter the name: ")
        if name in student:
            del student[name]
            print("Removed")
        else:
            print("Student not found")
        
        print()
    elif(choice=="6"): 
        if(student=={}):
            print("empty")
        else:
            import os
            print(os.getcwd())
            with open("students.json","w")as file:
                json.dump(student,file)
        print("Data saved successfully! ")
        print()
    elif(choice=="7"):
        try:
            with open("students.json","r")as file: 
                student=json.load(file)
            print(student)
        except FileNotFoundError:
            print("file not exists!")
        
    elif(choice=="8"):
        print("Exiting ")
        break
    else: 
        print("invalid choice")

        
