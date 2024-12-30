"""
*Створення профілів користувачів
 - Створіть файл profiles.json із наступним початковим вмістом:
 [
  {"name": "Alice", "age": 17, "hobbies": ["reading", "chess"]},
  {"name": "Bob", "age": 16, "hobbies": ["football", "gaming"]}
]

Напишіть програму, яка:
- Зчитує цей JSON-файл.
- Просить користувача ввести новий профіль:
    - Ім'я (рядок).
    - Вік (число).
    - Хобі (список хобі, розділених комами).
- Додає цей профіль до списку.
- Зберігає оновлений список у файл.

Приклад вводу користувачем:
Output:
Введіть ім'я: Charlie
Введіть вік: 15
Введіть хобі (через кому): painting, hiking

Результуючий файл profiles.json:
[
  {"name": "Alice", "age": 17, "hobbies": ["reading", "chess"]},
  {"name": "Bob", "age": 16, "hobbies": ["football", "gaming"]},
  {"name": "Charlie", "age": 15, "hobbies": ["painting", "hiking"]}
]
"""

import json
from pathlib import Path

files_dir = Path(__file__).absolute().parent / "files"
storage_file = files_dir / "profiles.json"


class ProfilesStorage:
    def __init__(self) -> None:
        self.users = self.read_json()

    @staticmethod
    def read_json():
        with open(storage_file, 'r') as file:
         return json.load(file)

    @staticmethod
    def write_json(users_list: list) -> None:
        with open(storage_file, mode="w") as file:
            return json.dump(users_list, file)

    def flush(self) -> None:
        self.write_json(self.users)

    def show_users(self):
        for user in self.users:
            print(f"{user['name']}, age: {user['age']}, hobbies: {",".join(user["hobbies"])}")

    def add_user(self, name, age, hobbies):
        for user in self.users:
            if user['name'] == name:
               print(f"User {name} already exists.")
               return
        new_user = {"name": name, "age": age, "hobbies": hobbies}
        self.users.append(new_user)

def user_input():
    storage = ProfilesStorage()

    print("Enter data for new user")
    name = input("Enter name: ")
    age = input("Enter age: ")
    if not age.isdigit() or not (1 <= int(age) <= 100):
        print ("Age should be a number (1-100)")
        return
    hobby_names = input("Enter hobbies, separated by a comma: ")
    if "," not in hobby_names:
        hobby_names = ",".join(hobby_names.split())
    hobbies = []
    for hobby in hobby_names.split(","):
        hobbies.append(hobby.strip())
    storage.add_user(name, age, hobbies)
    storage.flush()
    print(f"New user {name} is created")

user_input()