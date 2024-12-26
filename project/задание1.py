first_word = input("Введите первое слово (длиннее второго): ")
second_word = input("Введите второе слово: ")

# Проверка, что первое слово длиннее второго
if len(first_word) <= len(second_word):
    print("Первое слово должно быть длиннее второго.")
else:
    # Определяем количество символов, которые нужно заменить
    length_to_replace = len(second_word)

    # Заменяем символы во втором слове на первое слово
    modified_second_word = first_word[:length_to_replace] + second_word[length_to_replace:]

    # Вывод результата
    print("Результат:", modified_second_word)