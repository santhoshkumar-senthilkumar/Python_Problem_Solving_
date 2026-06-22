a=int(input("Enter a number : "))
rev=0
while a!=0:
    digit=a%10
    rev=digit+rev*10
    a=a//10
print("The Reverse of the input is : ",rev)
