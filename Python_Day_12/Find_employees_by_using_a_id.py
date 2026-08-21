a=int(input("Enter the number of employees : "))
employees=[]
idstart = 100
for i in range(a):
    b={}
    b["Id"] = idstart
    b["Name"]=input(f"Your id is {idstart} Enter the name : ")
    b["salary"]=int(input("Enter the salary : "))
    employees.append(b)
    idstart  += 1
search = int(input("Enter the ID to Search : "))
for i in employees:
    if i["Id"]==search:
        print(i)
        break;
