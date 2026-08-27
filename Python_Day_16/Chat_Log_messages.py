"""Given a chat log containing messages with usernames and timestamps,
extract each user and the messages they sent in a dictionary format."""
import re
text ="""[10:01] Alice: Hi Bob!
[10:02] Bob: Hey Alice!
[10:03] Alice: How are you?"""
a=re.findall(r"(?<=\]\s)\w+", text)
message=re.findall(r"(?<=:\s).*", text)
d={}
for i in range(len(a)):
    if a[i] not in d:
        d[a[i]]=message[i]
    elif a[i] in d:
        d[a[i]]+=message[i]
print(d)
        
    

