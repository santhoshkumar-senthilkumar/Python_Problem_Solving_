is999 = True
pos =0
neg =0
while(is999) :
    a=int(input("Enter a number 999 to stop this "))
    if a == 999 :
        print("Positive number you enterd : ",pos)
        print("Negative number you enterd : ",neg)
        break
    elif a<0 :
        neg += 1
    elif a>0 :
        pos += 1
