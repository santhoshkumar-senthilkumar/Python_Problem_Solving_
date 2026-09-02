'''Create a class TemplateEngine that replaces placeholders in a text using a dictionary of variables.
Placeholders are written in double curly braces {{variable_name}}.
Use regex to identify and replace them dynamically.
'''

import re
text = "Hello {{name}}, your order {{order_id}} will be delivered by {{date}}."
data = {"name": "Ravi", "order_id": "A1023", "date": "2025-10-06"}
sub = re.findall(r"{{(\w+)}}",text)
for i in sub:
    text=re.sub(r"{{(\w+)}}",data[i],text,1)
print(text)
