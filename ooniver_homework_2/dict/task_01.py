from random import randint

d = {}
for _ in range(10):
    key = randint(0, 99)
    value = key ** 3
    d[key] = value
print(f'My dictionary is --> {d}')

keys_to_remove = []
for key in d.keys():
    if not key % 2:
        keys_to_remove.append(key)

for key in keys_to_remove:
    del d[key]
print(f'Dict without even --> {d}')

keys_list = list(d.keys())
values_list = list(d.values())
for i in range(len(keys_list) - 1):
    for j in range(i + 1, len(keys_list)):
        if keys_list[i] < keys_list[j]:
            keys_list[i], keys_list[j] = keys_list[j], keys_list[i]
            values_list[i], values_list[j] = values_list[j], values_list[i]

print(f'Sorted key list --> {keys_list}')
print(f'Sorted values list --> {values_list}')
