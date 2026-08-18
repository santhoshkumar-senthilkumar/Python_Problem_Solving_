def func():
    a=input("Enter a Gender : ").upper()
    if a=="MALE":
        age = int(input("Enter a age : "))
        if age >=60 or age <=12 :
            conductor = input("I Am Your Friend means give yes : ").upper()
            if conductor == "YES" :
             print("Your ticket is free")
            else :
                print("Your ticket is half price")
        else :
         print("You Want to pay full Ticket price")
    elif a=="FEMALE" :
        print("Your ticket is free ")
    else :
        print("Invalid entry")
        func()
 
func()
