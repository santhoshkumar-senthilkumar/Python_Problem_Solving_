a=int(input("Enter the Size of the list : "))
b=[]
for i in range(a):
    b.append(int(input("Enter the number : ")))
for i in range(len(b)-1):
    if b[i] + 1 != b[i+1]:
        print("The Missing NUmber is " ,b[i] + 1)
        break
