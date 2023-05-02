dict_1 = dict(age=input('vozrast?'), name=input('imya?'), sname=input('familiya?'), work=input('rabota?'))

print(dict_1.get('work'),'\n', '-' * 10,'\n', dict_1.get('sname'), dict_1.get('name'), ', ', dict_1.get('age'), sep='')
