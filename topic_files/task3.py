"""
Облік відвідування занять

Створіть файл attendance.csv із наступними даними:
Name,Date,Status
Alice,2024-12-01,Present
Bob,2024-12-01,Absent
Alice,2024-12-02,Present
Bob,2024-12-03,Present
Напишіть програму, яка виконує наступне:
- Зчитує файл attendance.csv і виводить його вміст у зручному форматі.
- Просить користувача додати новий запис про відвідування:
    - Ім'я студента.
    - Дату (у форматі YYYY-MM-DD).
    - Статус (Present або Absent).
- Додає цей запис до файлу.
- Підраховує кількість відвідувань (Present) і пропусків (Absent) для кожного студента та виводить результати на екран.
- Після підрахунку відвідувань, програма додає нову колонку Comments до файлу, якщо її ще немає.
    Користувачеві пропонується ввести коментар для кожного запису у файлі.
"""

import csv
from pathlib import Path

class Attendance:
    def __init__(self):
        files_dir = Path(__file__).absolute().parent / "files"
        self.storage_file = files_dir / "attendance.csv"
        self.fieldnames = ["Name", "Date", "Status", "Comments"]

    def read_file(self):
        try:
            with open(self.storage_file) as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            return []

    def show_records(self):
        file_data = self.read_file()
        if file_data:
            for rec in file_data:
                print(f"{rec['Name']}, {rec['Date']}, {rec['Status']}")
        else:
            print ("File has no data")

    def write_file(self, file_data):
        with open(self.storage_file, mode="w") as file:
            writer = csv.DictWriter(file, self.fieldnames)
            writer.writeheader()
            writer.writerows(file_data)

    def add_attendance_record(self):
        file_data = self.read_file()

        name = input("Enter student's name: ")
        date = input("Enter date YYYY-MM-DD: ")
        status = input("Enter status Present or Absent: ")
        if status not in ["Present", "Absent"]:
            print("Invalid status")
            return

        for rec in file_data:
            if rec["Name"] == name and rec["Date"] == date:
                print("This record exists")
                return
        record = {"Name": name, "Date": date, "Status": status, "Comments": ""}
        file_data.append(record)
        self.write_file(file_data)
        print("New record is added.")

    def count_status(self):
        file_data = self.read_file()
        counted_status = {}
        for rec in file_data:
            name = rec["Name"]
            status = rec["Status"]
            if name not in counted_status:
                counted_status[name] = {"Present": 0, "Absent": 0}
            counted_status[name][status] += 1

        for name in counted_status:
            present_count = counted_status[name]["Present"]
            absent_count = counted_status[name]["Absent"]
            print(f"{name}: Present: {present_count}, Absent: {absent_count}")

    def add_comments(self):
        file_data = self.read_file()

        for rec in file_data:
            existing_comment = rec.get("Comments")
            if existing_comment:
                print(f"Record: {rec['Name']},date: {rec['Date']}, status: {rec['Status']}, Comment: {existing_comment}")
            new_comment = input(f"Enter new comment for {rec['Name']} : ")
            if new_comment:
                rec["Comments"] = new_comment
            print(f"Record: {rec['Name']},date: {rec['Date']}, status: {rec['Status']}, Comment: {new_comment}")
        self.write_file(file_data)
        print("Data is updated.")

    def main(self):
        while True:
            print("Available choice: 1 - Show records | 2 - Add new attendance record | 3 -Show attendance | 4 - Add comments | 5 - Exit ")

            choice = input("Enter your choice from 1 to 5: ")
            if choice == "1":
                 self.show_records()
            elif choice == "2":
                self.add_attendance_record()
            elif choice == "3":
                self.count_status()
            elif choice == "4":
                self.add_comments()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please, try again.")

if __name__ == "__main__":
    attendance = Attendance()
    attendance.main()