'''Write a class JSONSanitizer that takes a messy string containing pseudo-JSON data
and uses regex to clean it up into a valid JSON-like dictionary.
The input may contain extra spaces, single quotes, or trailing commas.'''

import re
text = { 'name': 'Alice', 'age': 25, 'skills': ['Python', 'ML', ], }
for i in text:
    print(i,":",text[i],)
