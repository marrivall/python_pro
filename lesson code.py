# """
# DRY: do not repeat yourself
# Student:
#     name: str
#     marks: list[int]
# Features:
# - fetch all students from the database
# - add another yet student to the database
# - retrieve the student by NAME. UI/UX issues...
# """
# COMMANDS = ("quit", "show", "retrieve", "add")
# # Simulated database
# students = [
#     {
#         "id": 1,
#         "name": "John Doe",
#         "marks": [4, 5, 1, 4, 5, 2, 5],
#         "info": "John is 22 y.o. Speciality: design",
#     },
#     {
#         "id": 2,
#         "name": "Marry Black",
#         "marks": [4, 1, 3, 4, 5, 1, 2, 2],
#         "info": "Marry is 23 y.o. Speciality: archeology",
#     },
# ]
#
# def find_student(name: str) -> dict | None:
#     for student in students:
#         if student["name"] == name:
#             return student
#     return None
#
# def find_student_by_id(student_id: int):
#     for student in students:
#         if student["id"] == student_id:
#             return student
#     return None
#
# def show_students() -> None:
#     print("=" * 20)
#     print("The list of students:\n")
#     for student in students:
#         print(f"{student['name']}. Marks: {student['marks']}")
#     print("=" * 20)
#
# def show_student(name: str) -> None:
#     student: dict | None = find_student(name)
#     if not student:
#         print(f"There is no student {name}")
#         return
#     print("Detailed about student:\n")
#     print(
#         f"{student['name']}. Marks: {student['marks']}\n"
#         f"Details: {student['info']}\n"
#     )
#
# def show_student_by_id(student_id: int) -> dict | None:
#     student = find_student_by_id(student_id)
#     if not student:
#         print(f"There is no student with this id")
#         return
#     else:
#         print("Detailed about student:\n")
#         print(
#             f"{student['name']}. Marks: {student['marks']}\n"
#             f"Details: {student['info']}\n"
#         )
#
# def add_student(student_name: str):
#     age = int(input("Enter student's age: "))
#     speciality = input("Enter student's speciality: ")
#     instance = {"name": student_name, "marks": [], "info": f"{age} y.o. speciality: {speciality}"}
#     students.append(instance)
#     return instance
#
# def main():
#     print(f"Welcome to the Digital journal!\nAvailable commands: {COMMANDS}")
#     while True:
#         user_input = input("Enter the command: ")
#
#         if user_input not in COMMANDS:
#             print(f"Command {user_input} is not available.\n")
#             continue
#
#         if user_input == "quit":
#             print("See you next time.")
#             break
#
#         try:
#             if user_input == "show":
#                 show_students()
#             elif user_input == "retrieve":
#                 choice = input("Search for a student by name or id?:")
#                 if choice == 'name':
#                     student_name = input("Enter student name you are looking for: ")
#                     show_student(student_name)
#                 elif choice == 'id':
#                     student_id = int(input("Enter student's id you are looking for: "))
#                     show_student_by_id(student_id)
#             elif user_input == "add":
#                 name = input("Enter student's name: ")
#                 add_student(name)
#         except NotImplementedError as error:
#             print(f"Feature '{error}' is not ready for live.")
#         except Exception as error:
#             print(error)
# main()

#####ДЗ №3########
"""
Student:
    name: str
    marks: list[int]

Features:
- fetch all students from the database
- add another yet student to the database
- retrieve the student by NAME. UI/UX issues...
"""

# ==================================================
# Simulated storage
# ==================================================
students = {
    1: {
        "name": "John Doe",
        "marks": [4, 5, 1, 4, 5, 2, 5],
        "info": "John is 22 y.o. Hobbies: music",
    },
    2: {
        "name": "Marry Black",
        "marks": [4, 1, 3, 4, 5, 1, 2, 2],
        "info": "Marry is 23 y.o. Hobbies: football",
    },
}

LAST_ID_CONTEXT = 2


def represent_students():
    for id_, student in students.items():
        print(f"[{id_}] {student['name']}, marks: {student['marks']}")


# ==================================================
# CRUD (Create Read Update Delete)
# ==================================================
def add_student(student: dict) -> dict | None:
    global LAST_ID_CONTEXT

    if len(student) != 2:
        return None
    elif not student.get("name") or not student.get("marks"):
        return None
    else:
        LAST_ID_CONTEXT += 1
        students[LAST_ID_CONTEXT] = student

    return student


def search_student(id_: int) -> dict | None:
    return students.get(id_)


def delete_student(id_: int):
    if search_student(id_):
        del students[id_]
        print(f"Student with id '{id_}' is deleted")
    else:
        print(f"There is no student '{id_}' in the storage")


def update_student(id_: int, payload: dict) -> dict:
    students[id_] = payload
    return payload


def student_details(student: dict) -> None:
    print(f"Detailed info: [{student['name']}]...")


# ==================================================
# Handle user input
# ==================================================
def parse(data: str) -> tuple[str, list[int]]:
    """Return student name and marks.

    user input template:
    'John Doe;4,5,4,5,4,5'


    def foo(*args, **kwargs):
        pass

    """

    template = "John Doe;4,5,4,5,4,5"

    items = data.split(";")

    if len(items) != 2:
        raise Exception(f"Incorrect data. Template: {template}")

    # items == ["John Doe", "4,5...."]
    name, raw_marks = items

    try:
        marks = [int(item) for item in raw_marks.split(",")]
    except ValueError as error:
        print(error)
        raise Exception(f"Marks are incorrect. Template: {template}") from error

    return name, marks


def ask_student_payload():
    """
    Input template:
        'John Doe;4,5,4,5,4,5'

    Expected:
        John Doe:       str
        4,5,4,5,4,5:    list[int]
    """

    prompt = "Enter student's payload using next template:\n'John Doe;4,5,4,5,4,5': "

    if not (payload := parse(input(prompt))):
        return None
    else:
        name, marks = payload

    return {"name": name, "marks": marks}

# ==================================================
# "Add Mark" feature
# ==================================================
def add_mark(id_: int, mark: int):
    student = search_student(id_)
    if not student:
        print(f"No student with id '{id_}'")
    else:
        try:
            student["marks"].append(mark)
            print(f"Mark {mark} is added to {student['name']}")
        except ValueError:
            print(f"❌ Invalid value")

# ==================================================
# "Partial Update" feature
# ==================================================
def student_partial_update(id_: int, name: str, marks: list[int]):
    student = search_student(id_)
    if student:
        if name and marks:
            student["name"] = name
            student["marks"] = marks
            print(f"Student's details are updated. Name:{student['name']}, marks:  {student['marks']}")
        elif name:
            student["name"] = name
            print(f"Updated student's name: {name} ")
        elif marks:
            student["marks"] = marks
            print(f"Updated student marks: {marks}")
    else:
        print(f"No student with id '{id_}'")


def handle_management_command(command: str):
    if command == "show":
        represent_students()

    elif command == "retrieve":
        search_id = input("Enter student's id to retrieve: ")

        try:
            id_ = int(search_id)
        except ValueError as error:
            raise Exception(f"ID '{search_id}' is not correct value") from error
        else:
            if student := search_student(id_):
                student_details(student)
            else:
                print(f"There is not student with id: '{id_}'")

    elif command == "remove":
        delete_id = input("Enter student's id to remove: ")

        try:
            id_ = int(delete_id)
        except ValueError as error:
            raise Exception(f"ID '{delete_id}' is not correct value") from error
        else:
            delete_student(id_)

    elif command == "change":
        update_id = input("Enter student's id you wanna change: ")

        try:
            id_ = int(update_id)
        except ValueError as error:
            raise Exception(f"ID '{update_id}' is not correct value") from error
        else:
            if data := ask_student_payload():
                update_student(id_, data)
                print(f"✅ Student is updated")
                if student := search_student(id_):
                    student_details(student)
                else:
                    print(f"❌ Can not change user with data {data}")

    elif command == "update details":
        enter_id = input("Enter student's id to update details: ")
        try:
            id_ = int(enter_id)
        except ValueError as error:
            raise Exception(f"❌ ID '{enter_id}' is not correct value") from error

        if student := search_student(id_):
            print("Choose what to update: name / marks/ name and marks: ")
            update_choice = input()

            if update_choice == "name":
                name_input = input("Enter new name: ")
                if name_input:
                    student["name"] = name_input
                    print(f"✅ Updated student's name: '{name_input}'")
            elif update_choice == "marks":
                marks_input = input("Enter new marks separated by a comma: ")
                if marks_input:
                    try:
                        marks = [int(mark) for mark in marks_input.split(",")]
                        student["marks"] = marks
                        print(f"✅ Updated student marks: {marks}")
                    except ValueError:
                        print("Marks should be separated by a comma")
            elif update_choice == "name and marks":
                name = input("Enter new name: ")
                if name:
                    student["name"] = name
                    print(f"✅ Updated student's name to '{name}'")
                marks_input = input("Enter new marks separated by a comma: ")
                if marks_input:
                    try:
                        marks = [int(mark) for mark in marks_input.split(",")]
                        student["marks"] = marks
                        print(f"✅ Updated student marks: {marks}")
                    except ValueError:
                        print("Marks should be separated by a comma")
            else:
                print("Invalid choice")
        else:
            print(f"No student with id '{id_}'")


    elif command == "add mark":
        input_id = input("Enter student's id to add mark: ")

        try:
            id_ = int(input_id)
        except ValueError as error:
            raise Exception(f"ID '{input_id}' is not correct value") from error

        input_mark = input("Add new mark: ")
        try:
            mark = int(input_mark)
        except ValueError as error:
            raise Exception(f"❌ Entered mark is not correct value") from error
        add_mark(id_, mark)

    elif command == "add":
        data = ask_student_payload()
        if data is None:
            return None
        else:
            if not (student := add_student(data)):
                print(f"❌ Can't create user with data: {data}")
            else:
                print(f"✅ New student '{student['name']}' is created")
    else:
        raise SystemExit(f"Unrecognized command: '{command}'")


def handle_user_input():
    """This is an application entrypoint."""

    SYSTEM_COMMANDS = ("quit", "help")
    MANAGEMENT_COMMANDS = ("show", "add", "retrieve", "remove", "change", "add mark", "update details")
    AVAILABLE_COMMANDS = SYSTEM_COMMANDS + MANAGEMENT_COMMANDS

    help_message = (
        "Welcome to the Journal application. Use the menu to interact with the application.\n"
        f"Available commands: {AVAILABLE_COMMANDS}"
    )

    print(help_message)

    while True:
        command = input("Enter the command: ")

        if command == "quit":
            print(f"\nThanks for using Journal application. Bye!")
            break
        elif command == "help":
            print(help_message)
        elif command in MANAGEMENT_COMMANDS:
            handle_management_command(command=command)
        else:
            print(f"Unrecognized command '{command}'")


handle_user_input()