from random import randint

list_1 = []
list_2 = []
for i in range(randint(1, 20)):
    list_1.append(randint(0, 100))

for i in range(randint(1, 20)):
    list_2.append(randint(0, 100))

if len(list_1) > len(list_2):
    keys = list_1
    values = list_2
else:
    keys = list_2
    values = list_1

d = {}
for i in range(len(keys)):
    if i < len(values):
        d[keys[i]] = values[i] / 2
    else:
        d[keys[i]] = 0
print(d)
