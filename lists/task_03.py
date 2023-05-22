from random import randint

n = 100
quantity = 3
first_matrix_list = [0] * quantity
second_matrix_list = [0] * quantity
third_matrix_list = [0] * quantity
square_matrix = []
min_list = []
max_list = []

for first_matrix_elems in range(quantity):
    first_matrix_list[first_matrix_elems] = randint(0, n)
print('first list -> ', first_matrix_list)

for second_matrix_elems in range(quantity):
    second_matrix_list[second_matrix_elems] = randint(0, n)
print('second list -> ', second_matrix_list)

for third_matrix_elems in range(quantity):
    third_matrix_list[third_matrix_elems] = randint(0, n)
print('third list -> ', third_matrix_list)

square_matrix.append(first_matrix_list)
square_matrix.append(second_matrix_list)
square_matrix.append(third_matrix_list)

print('square_matrix -> ', square_matrix)

min_list.append(min(square_matrix[0]))
min_list.append(min(square_matrix[1]))
min_list.append(min(square_matrix[2]))

max_list.append(max(square_matrix[0]))
max_list.append(max(square_matrix[1]))
max_list.append(max(square_matrix[2]))

print('minimum matrix element -> ', min(min_list))
print('maximum matrix element -> ', max(max_list))
