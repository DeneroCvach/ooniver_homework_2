# some_list = [1, 2, 3]
# list_counter = 0
#
# while list_counter < len(some_list):
#     print(some_list[list_counter] + 2)
#     list_counter += 1
# print(some_list)

# for i in range(len(some_list)):
#     print(some_list[i] + 2)
# print(some_list)

# list_1 = [1, 2, 3]
# list_2 = [1, 2, 4]
# if list_1 == list_2:
#     print('yes')
# else:
#     print('no')

#  СРЕЗЫ]!!!
# list_1 = [1, 2, 3, 4, 5, 6]
# list_2 = list_1[2:]
# list_3 = list_1[:4]
# list_4 = list_1[1:4]
# list_5 = list_1[1:6:2]
# list_6 = list_1[6:1:-2]
# print(list_1, list_3, list_4, list_5, list_6, sep="\n")

# list_a = [1, 2, 3]
# list_b = list_a[:] # ili cherez metod .copy
# list_a[0] = 9
# print(list_b)
# print(list_a)

# list_a = [1, 2, 3]
# list_b = [2, 3, 4]
# print(list_b)
# for elem in list_a:
#     list_b.append(elem)
# print(list_b)

# list_a = [1, 2, 3]
# elem = list_a.pop() # del list_a[1]

# str_1 = 'Александр Сергеевич Пушкин'
#
# second_letters = str_1.split('е')
# print(second_letters)

string = '''red, 
green, 
blue'''
print(len(string))