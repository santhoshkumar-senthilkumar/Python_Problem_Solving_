import re
 
files = [

    "Documents/report.pdf 500",

    "Documents/resume.docx 200",

    "Pictures/photo1.jpg 1500",

    "Pictures/photo2.jpg 2500",

    "Downloads/software.exe 4500",

    "Documents/project.pptx 800"

]

d={}

for i in files:

    s = i.split("/")

    if s[0] not in d:

        d[s[0]]=[]

        d[s[0]].append(s[1])

    elif s[0] in d:

        d[s[0]].append(s[1])

print(d)
 
