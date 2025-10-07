length = 78
width = 44
area = length * width
print(f"Площадь комнаты 1 {area}")

# function 
def great():
    """ Эта функция пишет привет """
    print("Привет это моя первая фукнкция")


# call func
great()



# name - argument func
def great(name):
    """ Эта функция пишет привет """
    print(f"Привет {name} это моя первая фукнкция")


great("Oleg")
great("nik")
great("man")


# function with any parameters
def introduce(name, age, city):
    """ Рассказа о человеке """
    print(f"Menya zovut {name}, mne {age} let, ya zhivu v city: {city}")

introduce("Lёnya", 42, "17")


########################################

def isAdult(age):
    if age >= 18:
        return True
    else:
        return False
    
if isAdult(50):
    print("access denied")
else:
    print("katis otsuda")

