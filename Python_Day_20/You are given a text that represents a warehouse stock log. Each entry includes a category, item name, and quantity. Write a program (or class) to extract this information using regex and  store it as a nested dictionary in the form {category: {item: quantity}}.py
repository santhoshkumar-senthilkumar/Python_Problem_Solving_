import re
 
data = """
Category: Electronics Item: Laptop Qty: 10
Category: Electronics Item: Phone Qty: 25
Category: Furniture Item: Chair Qty: 15
Category: Furniture Item: Table Qty: 5
"""
d= data.strip().split("\n")
dic={}
for i in d :
    Category = re.findall(r"Category:\s*(\w+)",i)[0]
    Item = re.findall(r"Item:\s*(\w+)",i)[0]
    Qty = re.findall(r"Qty:\s*(\d+)",i)[0]
    if Category not in dic:
        dic[Category] = {Item : Qty}
    elif Category in dic:
        dic[Category][Item] =Qty

for i in dic:
    print(i,dic[i])
