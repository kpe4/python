class Entity:
    #Свойства класса (общий для всех Pablo)

    #метод _init_ - конструктор который вызывается при создании обьекта
    def __init__ (self, name, health, attack_power):
        # ссылка на сам объект (на самого себя)
        # name, health, attack_power - параметры которые передаем при создании объекта

        self.name = name # просто даем имя персонажу
        self.health = health
        self.attack_power = attack_power
        self.healer = healer
        # level - параметр который не задается при создании объекта т е он будет иметь значение по умолчанию
        # и мы его будем рег прогаммно
        self.level = 1

        print(f"Character {self.name} is created! Health: {self.health} | Attack: {self.attack_power}")

    def attack(self, enemy):
        # self - тот кто атакует 
        # enemy - жертва 
        print(f"{self.name} attack {enemy.name} by {self.attack_power} damage")
        enemy.health -= self.attack_power

    def heal(self, amount):
        print(f"{self.name} is healing {self.healer}. Health: {self.health}")
        self.health += self.healer

# создание первого игрока по чертежу (шаблону) Entity
hero1 = Entity("Azazin Kreet", 80, 25)
# порядок действий python при создании объекта
# python  вызывает init 
# self = hero1 - новый объект
# параметры "Пабло Азазин", 80, 25 сохраняются в свойства объекта 
hero2 = Entity("Kamradio", 60, 15)

hero1.health = 120 # типа похилился

pablo = Entity("Pablo", 50, 10)

hero1.attack(pablo)

pablo.attack(hero1)