logs = [
    "John IN",
    "Alice IN",
    "John OUT",
    "John IN",
    "Alice OUT",
    "John OUT"
]
check_In ={}
check_out={}
for i in logs:
    d=i.split(" ")
    if d[1].upper() == "IN":
        if d[0] not in check_In:
            check_In[d[0]] = 1
        elif d[0] in check_In:
            check_In[d[0]] += 1
    elif d[1].upper() == "OUT":
        if d[0] not in check_out:
            check_out[d[0]] = 1
        elif d[0]in check_out:
            check_out[d[0]] += 1
print(check_In, check_out)
