
a=int(input("Enter the number of employees : "))
employees=[]
for i in range(a):
    b={}
    b["Name"]=input("Enter the name : ")
    b["salary"]=int(input("Enter the salary : "))
    employees.append(b)
highest=employees[0]
second = employees[0]
for i in employees:
    if i["salary"]>highest["salary"]:
        second =highest
        highest=i
    elif i["salary"]<highest["salary"] and i["salary"]>second["salary"]:
        second = i
print(second)
