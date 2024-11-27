"""
DRY: do not repeat yourself
Student:
    name: str
    marks: list[int]
Features:
- fetch all students from the database
- add another yet student to the database
- retrieve the student by NAME. UI/UX issues...
"""
COMMANDS = ("quit", "show", "retrieve", "add")
# Simulated database
students = [
    {
        "id": 1,
        "name": "John Doe",
        "marks": [4, 5, 1, 4, 5, 2, 5],
        "info": "John is 22 y.o. Speciality: design",
    },
    {
        "id": 2,
        "name": "Marry Black",
        "marks": [4, 1, 3, 4, 5, 1, 2, 2],
        "info": "Marry is 23 y.o. Speciality: archeology",
    },
]

def find_student(name: str) -> dict | None:
    for student in students:
        if student["name"] == name:
            return student
    return None

def find_student_by_id(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return None

def show_students() -> None:
    print("=" * 20)
    print("The list of students:\n")
    for student in students:
        print(f"{student['name']}. Marks: {student['marks']}")
    print("=" * 20)

def show_student(name: str) -> None:
    student: dict | None = find_student(name)
    if not student:
        print(f"There is no student {name}")
        return
    print("Detailed about student:\n")
    print(
        f"{student['name']}. Marks: {student['marks']}\n"
        f"Details: {student['info']}\n"
    )

def show_student_by_id(student_id: int) -> dict | None:
    student = find_student_by_id(student_id)
    if not student:
        print(f"There is no student with this id")
        return
    else:
        print("Detailed about student:\n")
        print(
            f"{student['name']}. Marks: {student['marks']}\n"
            f"Details: {student['info']}\n"
        )

def add_student(student_name: str):
    age = int(input("Enter student's age: "))
    speciality = input("Enter student's speciality: ")
    instance = {"name": student_name, "marks": [], "info": f"{age} y.o. speciality: {speciality}"}
    students.append(instance)
    return instance

def main():
    print(f"Welcome to the Digital journal!\nAvailable commands: {COMMANDS}")
    while True:
        user_input = input("Enter the command: ")

        if user_input not in COMMANDS:
            print(f"Command {user_input} is not available.\n")
            continue

        if user_input == "quit":
            print("See you next time.")
            break

        try:
            if user_input == "show":
                show_students()
            elif user_input == "retrieve":
                choice = input("Search for a student by name or id?:")
                if choice == 'name':
                    student_name = input("Enter student name you are looking for: ")
                    show_student(student_name)
                elif choice == 'id':
                    student_id = int(input("Enter student's id you are looking for: "))
                    show_student_by_id(student_id)
            elif user_input == "add":
                name = input("Enter student's name: ")
                add_student(name)
        except NotImplementedError as error:
            print(f"Feature '{error}' is not ready for live.")
        except Exception as error:
            print(error)
main()