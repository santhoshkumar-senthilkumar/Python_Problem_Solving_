def helpp (args) :
    lowest = args[0]
    for i in args:
        if i < lowest :
            lowest = i
    return lowest
a=[]
for i in range(5):
    b=int(input("Enter a number : "))
    a.append(b)
print(help(a))
