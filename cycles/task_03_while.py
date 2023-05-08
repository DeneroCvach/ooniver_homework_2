num_1 = int(input('Enter the number: '))
num_2 = int(input('Enter the number: '))
counter = num_1

if num_2 > num_1:
    while counter < num_2:
        if counter == 23 or counter == 32:
            break
        elif counter % 5:
            print(counter)
        counter += 1
else:
    print('Second value must be greater, then first!')
