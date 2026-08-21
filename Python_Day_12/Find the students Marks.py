a=int(input("Enter the number of students : "))
b=int(input("Enter the number of subjects : "))
students ={}
for i in range(a):
    name = input("Enter the name : ")
    if name not in students :
        marks=[]
        for i in range(b):
           marks.append(int(input("Enter the marks : ")))
    students[name]=marks
name = input("Enter a student name to see the marks : ")
if name in students:
    print(name,students[name])
else:
    print("Invalid student name ")
