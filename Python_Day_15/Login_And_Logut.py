import re

text = """[2025-10-05]
User: alice Action: login

[2025-10-05]
User: bob Action: upload

[2025-10-06]
User: alice Action: logout"""

users = re.findall(r"User:\s*(\w+)", text)
date = re.findall(r"\[(\d{4}-\d{2}-\d{2})\]",text)
action = re.findall(r"Action:\s*(\w+)",text)
print(action)
print(users)
print(date)
d = {}
for i in range(len(users)):
    if users[i] not in d:
        d[users[i]] = {date[i]: action[i]}
    elif users[i] in d:
        d[users[i]][date[i]] = action[i]

print(d)
