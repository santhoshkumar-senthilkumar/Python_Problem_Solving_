import re

text = "Meetings are on 2025-10-06, 10/07/2025, and 08-Nov-2025."

dates = re.findall(r'\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{2}-[A-Za-z]{3}-\d{4}', text)

d = {}

for i in range(len(dates)):
    d[i] = dates[i]

print(d)
