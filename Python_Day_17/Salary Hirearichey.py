
employees = {
"CEO": ["M1", "M2"],
"M1": ["E1", "E2"],
"M2": ["E3"],
"E1": [],
"E2": [],
"E3": []
}
salary = {
"CEO": 100,
"M1": 60,
"M2": 70,
"E1": 20,
"E2": 25,
"E3": 30
}
 
Count ={}
for i in employees:
    c=0
    for j in salary:
        if i == "CEO":
            c += salary[j]
        elif i == "M1":
            c += salary["E1"]
            c += salary["E2"]
        elif i == "M2":
            c += salary["E3"]
        elif i== 'E1' or i ==  'E2' or i == 'E3':
             c += salary[i]
             break
    Count[i] = c
print(Count)
