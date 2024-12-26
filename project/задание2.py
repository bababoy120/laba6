sentence = input("Введите предложение: ")

# Удаляем начальные пробелы и разбиваем предложение на слова
words = sentence.strip().split()

# Проверяем, есть ли первое слово
if words:
    first_word = words[0]
    # Подсчитываем количество букв 'о' в первом слове
    count_o = first_word.lower().count('о')
    print(f"Количество букв 'о' в первом слове: {count_o}")
else:
    print("В предложении нет слов.")