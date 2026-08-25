
# Frequency_of_The_Word

a = int(input("Enter the number of words: "))
b = []

for i in range(a):
    b.append(input())

c = {}

for i in b:
    if i not in c:
        c[i] = 1
    elif i in c:
        c[i] += 1

print(c)
