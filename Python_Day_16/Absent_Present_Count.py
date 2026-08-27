attendance = [
    "Arun:Present",
    "Bala:Absent",
    "Arun:Present",
    "Kumar:Present",
    "Bala:Present",
    "Arun:Absent",
    "Kumar:Present",
    "Bala:Absent",
    "Kumar:Absent"
]

d = {}

for item in attendance:
    name, status = item.split(":")
    if name not in d:
        d[name] = {"Present": 0, "Absent": 0}
    if status == "Present":
        d[name]["Present"] += 1
    else:
        d[name]["Absent"] += 1

high = 0
best = ""

for name in d:
    present = d[name]["Present"]
    absent = d[name]["Absent"]
    total = present + absent
    percentage = (present / total) * 100
    print(name, "-> Present:", present, ", Absent:", absent, ", Percentage:", round(percentage, 2), "%")
    if percentage > high:
        high = percentage
        best = name
print("Best Attendance:", best)
print("Percentage:", round(high, 2), "%")
