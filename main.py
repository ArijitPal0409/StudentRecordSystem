# main.py

from db import *

create_table()

def menu():
    while True:
        print("\n Student Record Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search by Roll")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == '1':
            name = input("Name: ")
            roll = input("Roll: ")
            department = input("Department: ")
            marks = int(input("Marks: "))
            insert_student(name, roll, department, marks)
            print(" Student added.")

        elif choice == '2':
            students = get_all_students()
            for stu in students:
                print(f"ID: {stu[0]}, Name: {stu[1]}, Roll: {stu[2]}, Dept: {stu[3]}, Marks: {stu[4]}")

        elif choice == '3':
            roll = input("Enter Roll No: ")
            student = search_by_roll(roll)
            if student:
                print(f"Name: {student[1]}, Dept: {student[3]}, Marks: {student[4]}")
            else:
                print(" Student not found.")

        elif choice == '4':
            roll = input("Roll No to Update: ")
            name = input("New Name: ")
            department = input("New Department: ")
            marks = int(input("New Marks: "))
            update_student(roll, name, department, marks)
            print(" Record updated.")

        elif choice == '5':
            roll = input("Roll No to Delete: ")
            delete_student(roll)
            print(" Record deleted.")

        elif choice == '6':
            print(" Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
