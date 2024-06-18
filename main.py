

import csv
from dataclasses import dataclass
from enum import Enum, auto
import logging
from typing import List

# 设置日志
logging.basicConfig(level=logging.INFO)



# 基础知识：类定义
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"{self.name}, {self.age}, {self.grade}"

# 进阶知识：装饰器
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

# 基础知识：异常处理
class InvalidAgeException(Exception):
    pass

# 基础知识：文件操作
def save_student(student):
    with open("./students.txt", "a") as file:
        file.write(str(student) + "\n")
        
# 进阶知识：使用csv模块
def save_students_csv(students: List[Student]):
    with open("./students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Grade"])
        for student in students:
            writer.writerow([student.name, student.age, student.grade])

# 进阶知识：列表推导式和异常处理
@log_decorator
def load_students():
    try:
        with open("./students.txt", "r") as file:
            all_data=[]
            for line in file:
                item=line.strip().split(", ")
                all_data.append(Student(item[0],item[1],item[2]))
            return all_data
    except FileNotFoundError:
        return []

# 基础知识：函数定义和循环
def main():
    while True:
        print("Student Information Management System")
        print("1. Add Student")
        print("2. List Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:#异常处理
                name = input("Enter student name: ")
                age = int(input("Enter student age: "))##提前设定了int类型
                grade = input("Enter student grade: ")
                if age < 0:
                    raise InvalidAgeException("Age cannot be negative")
                student = Student(name, age, grade)
                save_student(student)
                save_students_csv([student])
                print("Student added successfully.")
            except ValueError:
                print("Invalid input. Please enter numeric value for age.")
                logging.info("Invalid input. Please enter numeric value for age xxxx.")
            except InvalidAgeException as e:
                print(e)

        elif choice == "2":
            students = load_students()
            print(students)
            if students:
                for student in students:
                    print("all student:",student)
            else:
                print("No students found.")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
