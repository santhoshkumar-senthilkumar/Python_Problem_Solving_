#Find The lowest Digit in the number 

a=int(input("Enter a Number : "))

lowest = a%10

while a>0 :

    temp = a%10

    if temp<lowest :

        lowest = temp

    a//=10

print(lowest)
 
