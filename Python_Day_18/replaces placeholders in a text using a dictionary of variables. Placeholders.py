'''Create a class TemplateEngine that replaces placeholders in a text using a dictionary of variables.
Placeholders are written in double curly braces {{variable_name}}.
Use regex to identify and replace them dynamically.
'''

import re
text = "Hello {{name}}, your order {{order_id}} will be delivered by {{date}}."
data = {"name": "Ravi", "order_id": "A1023", "date": "2025-10-06"}
sub = re.sub(r"\{{name}}", data['name'],text)
sub = re.sub(r"\{{order_id}}", data['order_id'],sub)
sub = re.sub(r"\{{date}}", data['date'],sub)
print(sub)
