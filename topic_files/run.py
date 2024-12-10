import json
import csv
from pathlib import Path

# ==================================================
# Simulated storage
# ==================================================
files_dir = Path(__name__).absolute().parent / "files"
file_csv = files_dir / "students.csv"
storage_file = "students.json"

LAST_ID_CONTEXT = 2

class StudentsStorage:
    def __init__(self, file_type: str) -> None:
        if file_type == 'json':
            self.students = self.read_json(storage_file)
        elif file_type == 'csv':
            self.students = self.read_csv(file_csv, file_type)
        else:
            raise Exception (f"Incorrect file type: {file_type}")

    @staticmethod
    def read_json(filename: str) -> dict:
        try:
            with open(files_dir / filename) as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"file {filename} not found")
        except Exception as error:
            print(f"Can't read {filename}: {error}")

    @staticmethod
    def write_json(filename: str, data: dict) -> None:
        with open(files_dir / filename, mode="w") as file:
            return json.dump(data, file)

    @staticmethod
    def read_csv(filename: str, file_type: str) -> dict:
        try:
            with open(filename, mode="r") as file:
                reader = csv.DictReader(file)
                students = {}
                for row in reader:
                    student_id = row['id']
                    if student_id not in students:
                        students[student_id] = {"name": row["name"], "marks": row["marks"].split(",")}
            return students
        except FileNotFoundError:
            print(f"file {file_type} not found")
        except Exception as error:
            print(f"Can't read {file_type}: {error}")

    @staticmethod
    def write_csv(filename: str, data: dict) -> None:
        fieldnames = ["id", "name", "marks"]
        with open(filename, mode="w") as file:
            writer = csv.DictWriter(file, fieldnames)
            writer.writeheader()
            for id_, student in data.items():
                writer.writerow({"id": id_, "name": student["name"], "marks": ",".join(str(mark) for mark in student["marks"])})

    def flush(self, file_type) -> None:
        if file_type == 'json':
            self.write_json(storage_file, self.students)
        elif file_type == 'csv':
            self.write_csv(file_csv, self.students)
        else:
            raise Exception (f"Wrong file type: {file_type}")


def represent_students(file_type):
    for id_, student in StudentsStorage(file_type).students.items():
        print(f"[{id_}] {student['name']}, marks: {student['marks']}")


# ==================================================
# CRUD (Create Read Update Delete)
# ==================================================
def add_student(student: dict, file_type: str) -> dict | None:
    global LAST_ID_CONTEXT
    storage = StudentsStorage(file_type)

    if len(student) != 2:
        return None
    elif not student.get("name") or not student.get("marks"):
        return None
    else:
        LAST_ID_CONTEXT += 1
        storage.students[str(LAST_ID_CONTEXT)] = student

    storage.flush(file_type)
    return student


def search_student(id_: int, file_type) -> dict | None:
    storage = StudentsStorage(file_type)
    return storage.students.get(str(id_))


def delete_student(id_: int, file_type):
    storage = StudentsStorage(file_type)

    if search_student(id_, file_type):
        del storage.students[str(id_)]
        print(f"Student with id '{id_}' is deleted")
    else:
        print(f"There is student '{id_}' in the storage")


def update_student(id_: int, payload: dict, file_type: str) -> dict:
    storage = StudentsStorage(file_type)
    storage.students[str(id_)] = payload
    storage.flush(file_type)

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

def choose_file_type() -> str:
        file_type = input("Choose file type json or csv: ")
        if file_type != "json" and file_type != "csv":
            print ("Invalid file type. Try again")
        else:
             return file_type

def handle_management_command(command: str, file_type: str):
    if command == "show":
        represent_students(file_type)

    elif command == "retrieve":
        search_id = input("Enter student's id to retrieve: ")

        try:
            id_ = int(search_id)
        except ValueError as error:
            raise Exception(f"ID '{search_id}' is not correct value") from error
        else:
            if student := search_student(id_, file_type):
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
            delete_student(id_, file_type)

    elif command == "change":
        update_id = input("Enter student's id you wanna change: ")

        try:
            id_ = int(update_id)
        except ValueError as error:
            raise Exception(f"ID '{update_id}' is not correct value") from error
        else:
            if data := ask_student_payload():
                update_student(id_, data, file_type)
                print(f"✅ Student is updated")
                if student := search_student(id_, file_type):
                    student_details(student)
                else:
                    print(f"❌ Can not change user with data {data}")

    elif command == "add":
        data = ask_student_payload()
        if data is None:
            return None
        else:
            if not (student := add_student(data, file_type)):
                print(f"❌ Can't create user with data: {data}")
            else:
                print(f"✅ New student '{student['name']}' is created")
    else:
        raise SystemExit(f"Unrecognized command: '{command}'")


def handle_user_input():
    """This is an application entrypoint."""

    SYSTEM_COMMANDS = ("quit", "help")
    MANAGEMENT_COMMANDS = ("show", "add", "retrieve", "remove", "change")
    AVAILABLE_COMMANDS = SYSTEM_COMMANDS + MANAGEMENT_COMMANDS

    help_message = (
        "Welcome to the Journal application. Use the menu to interact with the application.\n"
        f"Available commands: {AVAILABLE_COMMANDS}"
    )
    print(help_message)

    file_type = choose_file_type()

    while True:
        command = input("Enter the command: ")

        if command == "quit":
            print(f"\nThanks for using Journal application. Bye!")
            break
        elif command == "help":
            print(help_message)
        elif command in MANAGEMENT_COMMANDS:
            handle_management_command(command=command, file_type=file_type)
        else:
            print(f"Unrecognized command '{command}'")


handle_user_input()