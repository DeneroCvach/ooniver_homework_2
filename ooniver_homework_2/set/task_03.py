text = '''У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил. '''

unique_chars = list(set(text))

sorted_chars = []
while unique_chars:
    min_ord = ord(unique_chars[0])
    min_char = unique_chars[0]
    for char in unique_chars:
        char_ord = ord(char)
        if char_ord < min_ord:
            min_ord = char_ord
            min_char = char
    sorted_chars.append(min_char)
    unique_chars.remove(min_char)

for char in sorted_chars:
    print(char, end=' ')

# еще один вариант решения, но немного попроще)))))

# sorted_chars = sorted(unique_chars, key=ord)
# for char in sorted_chars:
#     print(char, end=' ')
