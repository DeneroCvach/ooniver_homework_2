from random import randint

list_1 = []
list_2 = []
for _ in range(10):
    list_1.append(randint(0, 9))
    list_2.append(randint(0, 9))
print(list_1, list_2, sep='\n')

intersection = list(set(list_1).intersection(list_2))
difference = list(set(list_1).symmetric_difference(list_2))
unique_elem_list_01 = list(set(list_1) - set(list_2))
unique_elem_list_02 = list(set(list_2) - set(list_1))

print(f'Unic from first list --> {unique_elem_list_01}' if len(unique_elem_list_01) > 0 else 'No unic elements in list!')
print(f'Unic from second list --> {unique_elem_list_02}' if len(unique_elem_list_02) > 0 else 'No unic elements in list!')
print(f'Common elements --> {intersection}')
print(f'Difference elements --> {difference}')
