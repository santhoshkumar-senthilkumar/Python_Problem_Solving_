a=int(input("Enter a number : "))
rev=0
b=a
while a!=0:
    digit=a%10
    rev=digit+rev*10
    a=a//10
if b==rev:
    print(b,"The Number is Palindrome")
else :
    print(b,"It is not a palindrome")
