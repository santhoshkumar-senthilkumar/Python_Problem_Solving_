
a=int(input("Enter the size of the list : "))
b=[]
for i in range(a):
   b.append(input("Enter the word : "))
dic={}
for i in range(a) :
    group=[]
    for j in range(a):
        if b[i] not in group:
          group.append(b[i])
        if len(b[i]) == len(b[j]):
            if b[j] not in group:
               group.append(b[j])
        if len(b[i]) not in dic:
            dic[len(b[i])]=group
print(dic)
