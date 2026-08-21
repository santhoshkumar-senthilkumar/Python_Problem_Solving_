a=int(input("Enter the number of students : "))
b=int(input("Enter the number of subjects : "))
students ={}
Totalmarks=[]
for i in range(a):
    name = input("Enter the name : ")
    if name not in students :
        marks=[]
        total=0
        for i in range(b):
           marks.append(int(input("Enter the marks : ")))
           total += marks[i]
    students[name]=marks
    Totalmarks.append({"name": name ,"total" : total})
Highest=Totalmarks[0]
for i in Totalmarks:
    if Highest["total"]<i["total"]:
        Highest=i 
print(Highest)
