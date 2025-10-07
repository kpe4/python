book = {
    "title": "123123bom",
    "author": "жорж Оруэлл",
    "year": 1950,
    "ganre": "АнтиАнтония"
}

player = {
    "name": "Olegio",
    "damage": 20.3,
    "age": 52,
    "city": 17,
    "isAlive": True
}

simple = {
    1: "Один",
    2: "Два"
}

print(player["name"]) # Olegio

print(player.get("city")) # 17
print(player.get("class")) # none  (no error)
print(player.get("class", "No data"))

player["damage"] = 22.5

player["class"] = "Koldun"


# если внутри словаря plfyer естьключ name, то выполнить:
if "name" in player:
    print("Ключ nmae существует!")

if "HP" not in player:
    print("Ключ HP не найден!")\
    
# Deleting po key s vozvratom znacheniya
removed_value = player.pop("city")

# delete last item
last_item = player.popitem()
print("Удалили последнюю пару: ", last_item)

print(player.keys())
print(player.values())
print(player.items())

# Перебор словарей в циклах
# Перебор ключей словаря
for key in player.keys():
    print(key) # напечатает: name, age, damage .....

for value in player.values():
    print(value) # напечатает Olegio ..........

for key, value in player.items():
    print(f"Ключ {key}, Значение: {value}")

# spisok slovarey
students = [
    {"name": "Nikitos", "age": 15, "grades": [5,4,3,3,4,2]},
    {"name": "Vaneuk", "age": 64, "grades": [5,5,5,5,5,2]},
    {"name": "Sёma", "age": 7, "grades": [5,2,2,2,2,2]}
]

# polucheniye vozrasta pervogo studenta
print(students[0]["age"]) # 15
print(students[1]["name"]) # Vaneuk

# poluchit vse imena
for student in students:
    print(student["name"])
