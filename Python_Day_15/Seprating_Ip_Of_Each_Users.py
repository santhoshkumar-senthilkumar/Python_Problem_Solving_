import re

a = input()

user = re.findall(r"user:\s*(\w+)", a)
ip = re.findall(r"IP:\s*([0-9.]+)", a)

d = {}
print(user, ip)
for i in range(len(user)):
    if user[i] not in d:
        d[user[i]] = [ip[i]]
    elif ip[i] not in d[user[i]]:
        d[user[i]].append(ip[i])

print(d)
