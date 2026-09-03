data = """
ID: S101 Name: Alice Marks: 89
ID: S102 Name: Bob Marks: 76
ID: S103 Name: Carol Marks: 91
"""
 
students = {}
 
lines = data.strip().split("\n")
 
for i in lines:
 
    parts = i.split("ID:")
 
    if len(parts) > 1:
 
        info = parts[1].strip().split()
 
        sid = info[0]
        name = info[2]
        marks = int(info[4])
 
        students[sid] = {
            "name": name,
            "marks": marks
        }
 
print(students)
