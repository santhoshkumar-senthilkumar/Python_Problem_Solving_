logs = [
    "file1 v1",
    "file2 v1",
    "file1 v2",
    "file3 v1",
    "file1 v3",
    "file2 v2"
]
d ={}
for i in logs:
    s = i.split(" ")
    if s[0] not in d:
        d[s[0]]=[]
        d[s[0]].append(s[1])
    elif s[0] in d:
        d[s[0]].append(s[1])
print(d)
