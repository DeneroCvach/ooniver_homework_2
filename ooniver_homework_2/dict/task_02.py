from random import randint

students = []

stud_01 = {
    'Name': 'Anton',
    'Surname': 'Abramovich',
    'Age': 23,
    'Course': 3,
    'Math': randint(0, 10),
    'English': randint(0, 10),
    'PE': randint(0, 10)
}
students.append(stud_01)

stud_02 = {
    'Name': 'Alex',
    'Surname': 'Ciba',
    'Age': 22,
    'Course': 4,
    'Math': randint(0, 10),
    'English': randint(0, 10),
    'PE': randint(0, 10)
}
students.append(stud_02)

stud_03 = {
    'Name': 'Maria',
    'Surname': 'Klukva',
    'Age': 18,
    'Course': 1,
    'Math': randint(0, 10),
    'English': randint(0, 10),
    'PE': randint(0, 10)
}
students.append(stud_03)

for stud in students:
    avg_mark = (stud['Math'] + stud['English'] + stud['PE']) / 3
    stud['Average_mark'] = avg_mark
print(students)
