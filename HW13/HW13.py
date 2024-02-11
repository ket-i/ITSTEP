def student_info(my_dict):
    student_ids = [str(student["id"]) for student in my_dict["students"]]
    print(f"Student IDs: {student_ids} ")
    selected_id = input("airchiet studentis ID: ")
    
    
    selected_student = []
    
    for student in my_dict["students"]:
        if str(student["id"]) == selected_id:
            selected_student = student
            break
    
    if selected_student:
        print("\nStudent Information:")
        print("ID:", selected_student["id"])
        print("Name:", selected_student["name"].capitalize())
        print("Age:", selected_student["age"])

        print("\nSubject Grades:")
        for subject in my_dict["subjects"]:
            grade = subject["grades"].get(selected_id)
            print(f"Subject: {subject['name']}, Grade: {grade}")
    else:
        print("Invalid student ID")


my_dict = {
  "students": [
    {"id": 20, "name": "giorgi", "age": 25},
    {"id": 25, "name": "giorgi", "age": 23},
    {"id": 100, "name": "nika", "age": 22},
    {"id": 56, "name": "nika", "age": 25},
    {"id": 1232, "name": "dato", "age": 22},
    {"id": 846723, "name": "archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
  ]
}


student_info(my_dict)