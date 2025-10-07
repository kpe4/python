# vocabular
dictionary = {
    "яблоко": "apple",
    "банан": "banana",
    "киви": "kiwi",
    "apple":"яблоко",
    "pineapple":"ананас",
    "banana":"банан",
    "bicycle":"лисопед",
    "phone":"телефон",
    "shark":"акула",
    "shampaigne":"шампанское"
}

# цикл
for _ in iter(int, 1):
    word = input("Введите слово(Quit для выхода): ").strip().lower()
    if word == "quit":
        print("выход из программы, давай досвидания")
        break
    if word in dictionary:
        print(f"Перевод вашего слова: {dictionary[word]}")
    else:
        print("вашего слова нет в словаре")
        choice = input("добавите перевод? y/n ").strip().lower()
        if choice == "y":
            translation = input(f"Введите перевод слова '{word}': ").strip()
            dictionary[word] = translation
            print(f"Слово '{word}' с переводом '{translation}' добавлено в словарь.")
        else:
            print("ну ладно")


