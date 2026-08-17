a=int(input("Enter a number to reverse it : "))
c=0
while a>0 :
    temp = a%10
    c=c*10+temp
    a//=10
print(c)
