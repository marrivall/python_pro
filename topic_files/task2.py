"""
Створіть JSON-файл products.json із наступними даними:
[
    {"name": "Laptop", "price": 1200, "quantity": 5},
    {"name": "Headphones", "price": 100, "quantity": 50}
]
Напишіть програму, яка:
- Зчитує дані з файлу products.json.
- Перевіряє, чи кожен товар має ключ category. Якщо ключ відсутній, додає його зі значенням "Uncategorized".
"""
import json
from pathlib import Path

files_dir = Path(__file__).absolute().parent / "files"
storage_file = files_dir / "products.json"

class ProductsStorage:
    def __init__(self) -> None:
        self.products = self.read_json()

    @staticmethod
    def read_json():
        with open(storage_file, 'r') as file:
         return json.load(file)

    def write_json(self) -> None:
        with open(storage_file, mode="w") as file:
            return json.dump(self.products, file)

    def add_category(self):
        for product in self.products:
            if "category" not in product:
                product["category"] = "Uncategorized"
        self.write_json()
        print("New data is added")

storage = ProductsStorage()
storage.add_category()


