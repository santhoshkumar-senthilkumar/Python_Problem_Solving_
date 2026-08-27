fruits = [
    "apple:50",
    "banana:30",
    "apple:50",
    "orange:80",
    "banana:30",
    "apple:50"
]

d = {}

for item in fruits:
    name, price = item.split(":")
    price = int(price)

    if name not in d:
        d[name] = price
    else:
        d[name] += price

for name, price in d.items():
    print(name, "->", price)

high = 0
high_name = ""

for name, price in d.items():
    if price > high:
        high = price
        high_name = name

print("Highest Spending Product:", high_name)
print("Amount:", high)
