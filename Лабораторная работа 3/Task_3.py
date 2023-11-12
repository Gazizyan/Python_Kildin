# TODO  Напишите функцию count_letters
def count_letters(text):
    # меняем регистр всего текста на нижний
    lowercase_text = text.lower()
    letters_count = {}
    for letter in lowercase_text:
        if letter.isalpha():
            if letter in letters_count:
                letters_count[letter] += 1   # добавляем к уже существующей букве еще одну
            else:
                letters_count[letter] = 1    # либо если ее нет, даю ей значение 1

    return letters_count

# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters_count):
    total_letters = sum(letters_count.values())     # общее количество букв
    frequency_letters = {}      # создаем новый словарь, который будет состоять из строк буква : частота
    for one_letter, count in letters_count.items():
        frequency_letters[one_letter] = count / total_letters

    return frequency_letters


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
letters_count = count_letters(main_str)
frequency_letters = calculate_frequency(letters_count)

for letter, frequency in frequency_letters.items():
    print(f"{letter}: {frequency:.2f}")