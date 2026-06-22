a=int(input("Enter a Number : "))
sum=0
while a!=0:
    digit=a%10
    sum=sum+digit
    a=a//10
print("Sum of the digit is : ",sum)
