import os
import csv

path = 'files'

try:
    os.mkdir(path)
    print('Folder created\n')
except FileExistsError:
    print('Folder exists')
    print('Continue working...\n')

head = ["id", "name", "age", "grade", "subject_name", "marks"]

data = [
    [1, "John", 25, "A", "Astronomy", 90],
    [2, "Alice", 22, "B", "Physics", 85]
]

file_path = f"{path}/data3.csv"

with open(file_path, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(head)
    writer.writerows(data)

### 1 ###
def add_student_to_csv(file_path, id, name, age, grade, subject_name, marks):

    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([id, name, age, grade, subject_name, marks])


new_id = input("Enter ID: ")
new_name = input("Enter Name: ")
new_age = input("Enter Age: ")
new_grade = input("Enter Grade: ")
new_subject_name = input("Enter Subject Name: ")
new_marks = input("Enter Marks: ")

add_student_to_csv(file_path, new_id, new_name, new_age, new_grade, new_subject_name, new_marks)

### 2 ####
def read_all_students(file_path):
    with open(file_path, mode='r', encoding='utf-8', newline='') as file:
        reader = list(csv.DictReader(file))

        print(f"{'ID':<5} {'Name':<15} {'Age':<5} {'Grade':<5} {'Subject':<15} {'Marks'}")
        print("=" * 60)

        for row in reader:
            print(f"{row['id']:<5} {row['name']:<15} {row['age']:<5} {row['grade']:<5} {row['subject_name']:<15} {row['marks']}")

read_all_students(file_path)

def read_specific_student(file_path, student_id):
    with open(file_path, mode='r', encoding='utf-8', newline='') as file:
        reader = list(csv.DictReader(file))

        print(f"{'ID':<5} {'Name':<15} {'Age':<5} {'Grade':<5} {'Subject':<15} {'Marks'}")
        print("=" * 60)
        
        for row in reader:
            if row['id'] == student_id:
                print(f"{row['id']:<5} {row['name']:<15} {row['age']:<5} {row['grade']:<5} {row['subject_name']:<15} {row['marks']}")
                student_found = True
        

student_id = input("Enter ID: ")
read_specific_student(file_path, student_id)


### 3 ###
def update_student_score(file_path, student_id, subject_name, updated_score):

    with open(file_path, mode='r', encoding='utf-8', newline='') as file:
        reader = list(csv.DictReader(file))

 
    for row in reader:
        if row['id'] == student_id and row['subject_name'] == subject_name:
            row['marks'] = updated_score
            student_found = True
            break



    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        fieldnames = ["id", "name", "age", "grade", "subject_name", "marks"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(reader)

    print(f"Score for Student ID {student_id} in {subject_name} updated to {updated_score}.")


path = 'files'
file_path = f"{path}/data3.csv"

student_id_to_update = input("Enter the student ID ")
subject_to_update = input("Enter the subject to: ")
updated_score = input("Enter the updated score: ")

update_student_score(file_path, student_id_to_update, subject_to_update, updated_score)
