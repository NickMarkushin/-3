# TODO  Напишите функцию count_letters
def cpunt_letters(str):
    s = []
    a = str.lower()
    b = a.split()
    for i in b:
        for j in i:
            if j.isalpha():
                s += j
    str_ = set(s)
    letters = {}
    for i in str_:
        sum = 0
        for j in s:
            if i == j:
                sum += 1
        letters[i] = sum
    return letters


# TODO Напишите функцию calculate_frequency
def calculate_frequency(fun):
    vsego = sum(fun.values())
    for i in fun:
        fun[i] = round(fun.get(i) / vsego, 2)
    return fun


main_str = """
У лукоморья дуб зелёный;
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
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

letters = calculate_frequency(cpunt_letters(main_str))

for i in letters:
    g=format(letters.get(i),'.2f')
    print(f'{i}: {g}')
