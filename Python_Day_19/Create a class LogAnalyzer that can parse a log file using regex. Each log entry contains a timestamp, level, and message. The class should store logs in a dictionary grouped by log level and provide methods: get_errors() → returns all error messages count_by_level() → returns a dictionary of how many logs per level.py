import re 
log = """[2025-10-06 10:00] INFO Server started
[2025-10-06 10:05] ERROR Connection failed
[2025-10-06 10:10] INFO Retrying connection
[2025-10-06 10:12] DEBUG Retrying sequence
"""
messages = re.findall(r"\]\s+(\w+)", log)
d={}
for i in messages:
    if i not in d:
        d[i] = 1
    if i in d:
        d[i] += 1
print(d)
