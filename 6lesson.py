# open("что за файл", "что с ним делать", кодировка) - открыть и сохранить файл
# открытие файла для чтения
file = open("test.txt", "r", encoding="utf-8")
# read() - прочесть содержимое
content = file.read()
# файл важно закрыть после чтения
file.close()

print(content)

# with - безопасное чтение файла с последующим закрытием его
with open("test.txt", "r", encoding="utf-8") as file:
    content = file.read()
# файл гарантированно закроется после выхода из блока with

# "r" - чтение read 
# "w" - запись write
# "a" - добавление в конец файла
# "r+" - чтение и запись

# режим "w" - перезапись файла (если существует - перезапишется если его нет создастся)
with open("output.txt", "w", encoding="utf-8") as file:
        # \n - спец символ для отступа на след строку имитация enter
        # .write() - запись строки в файл
        file.write("привет это мое первое изм файла\n")
        file.write("а это моя вторая записанная строка\n")

# режим "a" - добавление в конец файла
with open("output.txt", "a", encoding="utf-8") as file:
      file.write("а это моя 3 строка, я добавил ее позже")

# === методы чтения файлов ===
with open("example.txt", "r", encoding="utf-8") as file:
    # read - читает файл как одну строку
    content = file.read()
    print("весь файл:")
    print(content)

# чтение только одной строки
with open("example.txt", "r", encoding="utf-8") as file:
    line1 = file.readline()
    line2 = file.readline()
    print("первая строка ", line1)
    print("вторая строка ", line2)
    
# readlines() - читает все строки как элементы списка
with open("example.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print("все строки как список:")
    for line in lines:
        print(line.strip()) # strip() убирает пробелы и переносы строк


        