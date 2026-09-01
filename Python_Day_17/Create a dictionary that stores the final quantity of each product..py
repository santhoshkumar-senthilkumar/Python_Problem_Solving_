import re
 
transactions = [
"Laptop +5",
"Phone +3",
"Laptop -2",
"Tablet +4",
"Phone -1",
"Laptop +1"
]
total ={}
for i in transactions:
    d = i.split(" ")
    if d[0] not in total:
        total[d[0]] = int(d[1])
    elif d[0] in total:
       total[d[0]] += int(d[1])
print(total)
