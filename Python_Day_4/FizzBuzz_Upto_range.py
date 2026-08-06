a=int(input("Enter a number for find a fizz , buzz and fizzbuzz"))
for i in range (1,a+1) :
    if i%3 ==0 and i%5 ==0 :
        print("FizzBuzz ", i)
    elif i%3 ==0 :
        print("Fizz" ,i)
    elif i%5 ==0 :
        print("Buzz ", i)
    else :
        print(i)
