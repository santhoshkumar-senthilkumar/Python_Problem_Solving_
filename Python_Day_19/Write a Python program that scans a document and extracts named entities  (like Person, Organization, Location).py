'''Write a Python program that scans a document and extracts named entities 
(like Person, Organization, Location) using provided tags, and organizes them in a dictionary.
Example Input:
text = "Alice(PERSON) works at Google(ORG) in California(LOC). Bob(PERSON) joined Amazon(ORG)."
'''
 
import re
 
text = "Alice(PERSON) works at Google(ORG) in California(LOC). Bob(PERSON) joined Amazon(ORG)."
PERSON = re.findall(r'(\w+)\(PERSON\)', text)
ORG=re.findall(r'(\w+)\(ORG\)', text)
LOC=re.findall(r'(\w+)\(LOC\)', text)
d={
    "PERSON":PERSON,
    "ORG":ORG,
    "LOC":LOC
}
print(d)
