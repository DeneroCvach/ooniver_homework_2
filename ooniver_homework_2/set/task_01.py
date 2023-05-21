from random import randint

list_1 = []
for i in range(100):
    list_1.append(randint(10, 99))
print(set(list_1))
