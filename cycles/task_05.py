k = 0

for number in range(0, 1000):
    counter = 0
    for digit in str(number):
        counter += int(digit)
    if counter > 1:
        for simple in range(2, counter):
            if counter % simple == 0:
                k = k + 1
        if k == 0:
            print(number, '->', counter)
        else:
            k = 0
