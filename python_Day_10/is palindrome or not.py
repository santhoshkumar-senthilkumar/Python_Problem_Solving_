a=input("Enter the word wheather the input is palindrome or not : ")
isbool = True
b=len(a)-1
for i in range(len(a)):
    if a[i]!=a[b]:
        isbool = False
        break
    else :
        b -=1
a = print("palindrome") if isbool else print("NOt a palindrome")
