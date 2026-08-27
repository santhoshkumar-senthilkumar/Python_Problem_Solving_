import re

log = """
[2025-10-01] Module: auth Time: 2.5s
[2025-10-01] Module: db Time: 1.8s
[2025-10-01] Module: auth Time: 3.1s
[2025-10-02] Module: db Time: 2.0s
"""
dates = re.findall(r"(?<=\[)\d{4}-\d{2}-\d{2}(?=\])", log)
modules = re.findall(r"(?<=Module: )\w+", log)
times = re.findall(r"(?<=Time: )[\d.]+(?=s)", log)

print(dates)
print(modules)
print(times)
d = {}

for i in range(len(dates)):

    date = dates[i]
    module = modules[i]
    time = float(times[i])

    if date not in d:
        d[date] = {}

    if module not in d[date]:
        d[date][module] = []

    d[date][module].append(time)
result = {}

for date in d:
    result[date] = {}

    for module in d[date]:
        values = d[date][module]

        average = sum(values) / len(values)

        result[date][module] = round(average, 1)

print(result)
