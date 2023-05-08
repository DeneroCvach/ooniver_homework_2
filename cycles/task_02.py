number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(number_list)):
    if not i % 2:
        print(number_list[i], number_list[i])
    elif i % 2:
        print(number_list[i] ** number_list[i])
