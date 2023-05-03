user_1 = dict(age=input('vozrast?'), name=input('imya?'), sname=input('familiya?'), work=input('rabota?'))
user_2 = dict(age='28', name='Andrey', sname='Petrov', work='ment')

print(user_1.get('work'), '\n', '-' * 10, '\n', user_1.get('sname'), user_1.get('name'), ', ', user_1.get('age'),
      sep='')

a = int(user_2["age"])
b = int(user_1["age"])

avg = int((a + b) / 2)

print(avg)