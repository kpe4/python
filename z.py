# n1
with open("numbers.txt", "w", encoding="utf-8") as file:
    for i in range(1, 11):
            file.write(f"{i}\n")

# n2
with open("numbers.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        line = line.strip() 
        if line.isdigit():   
            total += int(line)

print(f"сумма чисел: {total}")
