a=int(input("Enter a number : "))
count=0
while a!=0:
    a=a//10
    count+=1

print("The Digits of given number is : ",count)
