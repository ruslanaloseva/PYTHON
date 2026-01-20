# Функция подсчёта букв
de count_letters(text):
    letters_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            letters_count[char] = letters_count.get(char, 0) + 1
    return letters_count


# Функция вычисления частоты букв
def calculate_frequency(letters_dict):
    total_letters = sum(letters_dict.values())
    frequency_dict = {}

    for letter, count in letters_dict.items():
        frequency_dict[letter] = count / total_letters

    return frequency_dict


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

# Подсчёт и вычисление частот
letters_count = count_letters(main_str)
letters_frequency = calculate_frequency(letters_count)

# Печать результата в столбик
for letter, freq in sorted(letters_frequency.items()):
    print(f"{letter}: {freq:.2f}")
о