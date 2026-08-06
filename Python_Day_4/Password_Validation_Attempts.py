username ="santhosh"
password ="sandy"
a=3
for i in range (a) :
    b = input("Enter a Username : ")
    c = input("Enter a password : ")
    if b == username and c == password :
        print("Your Login Completed Successfully")
        break
    else :
        print(a)
        a=a-1
        print("Username or password invalid You left a ",a ," Attempt")
