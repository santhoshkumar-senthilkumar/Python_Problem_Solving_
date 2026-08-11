a=int(input("Enter a number : "))
number_of_digits = 0
sum_of_digits = 0
even_digits = 0
odd_digits = 0
while a!=0 :
    number_of_digits += 1
    b=int(a%10)
    print(b)
    sum_of_digits += b
    if b % 2 == 0 :
        even_digits += 1
    else :
        odd_digits += 1
    a=a//10
print(f"number of digits {number_of_digits}\n sum of digits {sum_of_digits} \n even digits {even_digits} \n odd digits {odd_digits}")
