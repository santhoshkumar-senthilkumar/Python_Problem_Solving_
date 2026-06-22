a=int(input("Enter a number : "))
large=0
while a!=0 :
    digit=a%10
    if digit>large :
        large = digit
    a=a//10
print("The Largest Digit in the number is : ",large)
