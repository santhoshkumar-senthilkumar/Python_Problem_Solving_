'''Create two dictionaries from separate text logs using regex extraction,
then merge them intelligently based on a shared key (user_id).
The class DataMerger should handle conflicts by choosing the latest timestamp entry.'''

import re
log1 = """
user:101 name:Ravi time:10:00
user:102 name:Kumar time:10:10"""
log2 = """
user:101 age:30 time:10:05
user:102 age:28 time:09:50"""
log1 = log1.strip().split("\n")
log2 = log2.strip().split("\n")
dic1 = {}
dic2 = {}
for i in log1:

    user_id = re.findall(r"user:(\d+)", i)[0]
    name = re.findall(r"name:(\w+)", i)[0]
    time = re.findall(r"time:(\d+:\d+)", i)[0]

    dic1[user_id] = {
        "name": name,
        "time": time
    }
for i in log2:

    user_id = re.findall(r"user:(\d+)", i)[0]
    age = re.findall(r"age:(\d+)", i)[0]
    time = re.findall(r"time:(\d+:\d+)", i)[0]

    dic2[user_id] = {
        "age": int(age),
        "time": time
    }
print("Log 1:", dic1)
print("Log 2:", dic2)
final = {}
for user_id in dic1:
    if user_id in dic2:
        if dic1[user_id]["time"] > dic2[user_id]["time"]:
            latest_time = dic1[user_id]["time"]
        else:
            latest_time = dic2[user_id]["time"]

        final[user_id] = {
            "name": dic1[user_id]["name"],
            "age": dic2[user_id]["age"],
            "time": latest_time
        }
    else:
        final[user_id] = dic1[user_id]
for user_id in dic2:

    if user_id not in final:
        final[user_id] = dic2[user_id]


print("Final:", final)
