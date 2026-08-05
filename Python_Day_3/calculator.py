a=int(input("Enter a number : "))
b=str(input("Enter a one operator to perform  /,*,+,- : "))
c=int(input("Enter a number : "))
if b == '/' :
    print(a/c)
elif b == '*' :
    print(a*c)
elif b == '-' :
    print(a-c)
elif b == '+' :
    print(a+c)
else :
    print("Invalid operator you have enterd")



