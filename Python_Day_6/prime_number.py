a=int(input("Enter a range to find the prime number : "))
for i in range (2,a) :
    isprime = True
    j=2
    while j<i:
        if i % 2 == 0 :
            isprime = False
            break
        j +=1
    if isprime :
        print(i)

    
