import re
 
data = """
Username: john Email: john@example.com Phone: 9876543210
Username: anna Email: anna@@example Phone: 12345
Username: mark Email: mark@gmail.com Phone: 9123456789
"""
 
users = {}
 
lines = data.strip().split("\n")
 
for i in lines:
 
    username = re.findall(r"Username:\s*(\w+)", i)
    email = re.findall(r"Email:\s*([\w.-]+@[\w.-]+\.\w+)", i)
    phone = re.findall(r"Phone:\s*(\d{10})", i)
 
    if username and email and phone:
 
        users[username[0]] = (email[0], phone[0])
 
print(users)
