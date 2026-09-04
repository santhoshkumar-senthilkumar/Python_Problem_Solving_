import re
 
data1 = "ID101: $50, ID102: $75, ID103: $100"
data2 = "ID102: $65, ID104: $120, ID101: $55"
data = data1 + data2
dc=re.findall(r"(ID\d+):\s*\$(\d+)", data)
d={}
divisor ={}
for i in dc:
        if i[0] not in d:
            d[i[0]] = int(i[1])
            divisor[i[0]] =1
        elif i[0] in d:
            d[i[0]] += int(i[1])
            divisor[i[0]] += 1
for i in d:
    d[i] = d[i]/divisor[i]
print(d)
