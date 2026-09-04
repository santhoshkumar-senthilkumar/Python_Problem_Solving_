import re
 
log = """
[INFO] System started
[DEBUG] Loading configuration
[ERROR] Connection failed
[INFO] Retrying connection
"""
 
d = {}
 
lines = log.strip().split("\n")
 
for line in lines:
 
    match = re.search(r"\[(.*?)\]\s+(.*)", line)
 
    if match:
 
        key = match.group(1)
        value = match.group(2)
 
        if key in d:
            d[key].append(value)
        else:
            d[key] = [value]
for i in d:
    print(i,d[i])
