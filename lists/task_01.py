from random import randint

n = 100
quantity = 10
worked_list = [0] * quantity
even_list = []
list_ending_with_7 = []

for i in range(quantity):
    worked_list[i] = randint(0, n)
print(worked_list)

max_elem = worked_list[0]
min_elem = worked_list[0]

for elem in worked_list:
    if not elem % 2:
        even_list.append(elem)
    elif elem % 10 == 7:
        list_ending_with_7.append(elem)
    if elem > max_elem:
        max_elem = elem
    elif elem < min_elem:
        min_elem = elem

print('multiple of seven list is -> ', list_ending_with_7)
print('even list is -> ', even_list)
print('minimum comparison operations edition -> ', min_elem)
print('maximum comparison operations edition -> ', max_elem)
print('minimum list element function edition -> ', min(worked_list))
print('maximum list element function edition -> ', max(worked_list))
