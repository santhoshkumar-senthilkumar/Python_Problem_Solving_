import re

text = input()

d = {
    ":)": "smile",
    ":(": "sad",
    "<3": "Love"
}

emojis = re.findall(r'(:\)|:\(|<3)', text)

for i in emojis:
    text = text.replace(i, d[i])

print(text)
