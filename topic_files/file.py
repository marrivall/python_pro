import json
from pathlib import Path

files_dir = Path(__name__).absolute().parent / "files"
csv_file = files_dir / "students.csv"
json_file = "students.json"

with open(files_dir / students) as file:
    data = json.load(file)
    print(data)
