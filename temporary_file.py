dict_1 = dict(age=input('vozrast?'), name=input('imya?'), sname=input('familiya?'), work=input('rabota?'))
user_2 = dict(age='28', name='Andrey', sname='Petrov', work='ment')

print(dict_1.get('work'),'\n', '-' * 10,'\n', dict_1.get('sname'), dict_1.get('name'), ', ', dict_1.get('age'), sep='')

a = int(user_2["age"])
b = int(dict_1["age"])

print((a + b)/2)