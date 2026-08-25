import re

text = input()

matches = re.findall(r'\(?\d{5}\s?\d{5}\)?|\d{3}-\d{3}-\d{4}|\d{10}', text)

d = {}

for num in matches:
    clean = re.sub(r'\D', '', num)

    if len(clean) == 10:
        d[clean[-4:]] = clean

print(d)
