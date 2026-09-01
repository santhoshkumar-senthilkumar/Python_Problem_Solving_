sales = [
"Laptop 50000",
"Phone 30000",
"Laptop 45000",
"Tablet 20000",
"Phone 25000",
"Laptop 55000"
]
total ={}
for i in sales:
    d = i.split(" ")
    if d[0] not in total:
        total[d[0]] = int(d[1])
    elif d[0] in total:
       total[d[0]] += int(d[1])
high =0
for i in total:
    if total[i]>high:
        high= total[i]
print(high)
