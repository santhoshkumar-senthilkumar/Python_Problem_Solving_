import re
input = "Alice: 89, Bob: 76, Charlie: 92, Alice: 95, Bob: 82"
student = re.findall(r"\w+(?=:)", input)
mark = re.findall(r"\d+", input)
d = {}
for i in range(len(student)):
    count = 0
    summ = 0
    for j in range(len(student)):
        if student[i] == student[j]:
            summ += int(mark[j])
            count += 1
    average = summ / count
    if student[i] not in d:
        d[student[i]] = average

print(d)
