"""
Аналіз доходів

Створіть файл income.csv із наступними даними:

Month,Income
January,2000
February,1800
March,2200

Напишіть програму, яка виконує наступне:
- Додавання даних за новий місяць:
    - Програма запитує у користувача назву місяця та суму доходу.
    - Новий запис додається у файл income.csv

- Розрахунок середнього доходу:
    - Програма читає всі записи та обчислює середнє значення доходу.

- Визначення місяця з найвищим доходом:
    - Програма знаходить місяць із найбільшим доходом та виводить цю інформацію.
"""

import csv
from pathlib import Path

class Incomes:
    def __init__(self):
        files_dir = Path(__file__).absolute().parent / "files"
        self.storage_file = files_dir/ "income.csv"
        self.fieldnames = ["Month", "Income"]

    def read_csv(self):
        try:
            with open(self.storage_file) as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            return []

    def show_data(self):
        data = self.read_csv()
        for rec in data:
            print(f"{rec['Month']} = {rec['Income']}")

    def write_csv(self, data):
        with open(self.storage_file, mode="w") as file:
            writer = csv.DictWriter(file, self.fieldnames)
            writer.writeheader()
            writer.writerows(data)

    def add_data(self):
        data = self.read_csv()
        try:
            month = input("Enter current month: ")
            income = int(input("Enter month's income: "))
            data.append({"Month": month, "Income": income})
            self.write_csv(data)
        except ValueError:
            print("Invalid value. Income should be a number")

    def average_income(self):
        data = self.read_csv()
        total_inc= 0
        for rec in data:
            total_inc += int(rec["Income"])
        average_inc = total_inc/len(data)
        print(f"Average income = {average_inc}")

    def highest_income(self):
        data = self.read_csv()
        highest_income = None
        highest_income_month = None
        for rec in data:
            current_inc = int(rec["Income"])
            if not (highest_income is not None and highest_income >= current_inc):
                highest_income = current_inc
                highest_income_month = rec["Month"]
        print(f"Highest income month is: {highest_income_month}, its income = {highest_income}")

    def main(self):
         while True:
             print("Available commands: 1 - show data | 2 - add income data | 3 -  average_income | 4 - the highest income month | 5 - exit: " )
             command = input("Enter your command: ")
             if command == "1":
                 self.show_data()
             elif command == "2":
                 self.add_data()
             elif command == "3":
                 self.average_income()
             elif command == "4":
                 self.highest_income()
             elif command == "5":
                 break
             else:
                 print(f"Invalid command. Please, enter available command")

if __name__ == "__main__":
    income_file = Incomes()
    income_file.main()