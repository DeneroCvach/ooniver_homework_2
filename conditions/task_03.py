user_age = int(input('Enter your age: '))

if user_age < 18:
    print('you are too young to work with this program!')
elif user_age > 65 :
    print('you are too old to work with this program')
elif 18 <= user_age <= 65:
    from antigravity import geohash
    print('welcome!')
