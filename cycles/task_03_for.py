num_1 = int(input('Enter the number: '))
num_2 = int(input('Enter the number: '))

if num_2 > num_1:
    for i in range(num_1, num_2):
        if i == 23 or i == 32:
            break
        elif i % 5:
            print(i)
else:
    print('Second value must be greater, then first!')
