"""Write a Python program to:

Split the sentence into individual words.
Count how many times each word appears.
Store the result in a dictionary.
Find the word that appears most frequently.
Print the frequency of every word and the most frequent word."""

a=input()
b=a.split(" ")
c={}
for i in b:
    if i not in c:
        c[i]=1
    elif i in c:
        c[i] +=1
for i in c:
    print(i,"->",c[i])
