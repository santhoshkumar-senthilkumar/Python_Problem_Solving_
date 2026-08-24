import re
a=input("Enter your paragraph : ")
b= re.findall(r"\d+\.?\d*", a)
d={}
for i in b:
    if i not in d:
            print(i)
            d[i] = 1
    elif i in d :
             d[i] += 1
print(d)
