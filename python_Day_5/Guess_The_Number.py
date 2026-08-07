a = 17
guess = True
while guess :
    b=int(input("Guess the Number : "))
    if b == a :
        print("Your guess is correct ")
        guess = False
    elif b > a :
        print("It is high : ")
    elif b < a :
        print("It is Low : ")
        
