# пустой спис
empty_list = []

fruits = ["apple","banana","dikiy ogurec"]

mixed_list = [1, "hello", 3.14, True]

number = list([1,2,3,4,5])

print(fruits[2])

print(fruits[-1])

# добавление 

print(fruits)

fruits.append("mambastic")

print(fruits)

fruits.insert(1, "kiwi")

print(fruits)

fruits.remove("kiwi")

print(fruits)

pop_res = fruits.pop(-1)

print("Удален: ", pop_res)

print(fruits)


numbers = [0,1,2,3,4,5,6,7,8,9]

print(numbers[2:5])

print(numbers[:5])

print(numbers[5:])

print(numbers[::2])

print(numbers[::-1])

for fruit in fruits: # для каждого фрукта в списке
    print("Я: ", fruit)

list_length = len(fruits)
print(list_length)

for i in range(len(fruits)):
    print("Index", i, "-is", fruits[i])
    
prices = [100, 200, 300, 40]

total = 0

for price in range(len(prices)):
    total = total + prices[i]
print("Сумма всех цен:", total)




