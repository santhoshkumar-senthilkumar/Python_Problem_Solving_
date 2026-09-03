'''You are given a paragraph of text.
Write a program to create a reverse index dictionary where:
Each word (case-insensitive) is a key
The value is a list of sentence numbers where the word appears'''
import re
 
text = "Python is great. I love Python programming. Great tools exist for Python."
 
t = text.split(".")
over = {}
count = 0
for i in t:
    if i.strip() == "":
        continue
    count += 1
    for j in i.lower().split():
        if j not in over:
            over[j] = [count]
        elif j in over:
            over[j].append(count)
print(over)
