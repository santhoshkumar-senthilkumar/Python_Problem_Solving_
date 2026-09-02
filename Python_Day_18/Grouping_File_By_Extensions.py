'''You’re given multiple lines describing file details in a log.
Each line contains a filename, extension, size (in KB), and modified date.
Use regex to parse and store the data in a dictionary grouped by file extension.'''

import re

data = """file1.txt size:12KB modified:2025-10-05
report.pdf size:230KB modified:2025-09-30
notes.txt size:8KB modified:2025-10-06
image.png size:1024KB modified:2025-08-20"""

data = data.split("\n")

result = {}

for i in data:

    name = re.findall(r"(\w+)\.", i)[0]
    extension = re.findall(r"\.(\w+)", i)[0]
    size = re.findall(r"size:(\d+)", i)[0]
    date = re.findall(r"\d{4}-\d{2}-\d{2}", i)[0]

    file_data = {
        "name": name,
        "size": int(size),
        "modified": date
    }

    if extension not in result:
        result[extension] = []

    result[extension].append(file_data)

for i in result:
    print(i,result[i])
