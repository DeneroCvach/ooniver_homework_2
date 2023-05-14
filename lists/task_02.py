from random import randint

n = 100
quantity = 10
worked_list = [0] * quantity

for i in range(quantity):
    worked_list[i] = randint(0, n)
worked_list.sort()
print('ascending list ->', worked_list)
