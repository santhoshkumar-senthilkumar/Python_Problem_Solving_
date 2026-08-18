a=int(input("Enter the size of the list : "))
b=[]
for i in range(a):
    b.append(int(input("ENter a number ")))
conhigh =0
for i in range(a):
    high=1
    gh=b[i]
    for j in range(a):
        if gh+1 in b :
            high += 1
            gh = gh+1
    if high > conhigh and high>1 :
        conhigh = high
print(conhigh)
