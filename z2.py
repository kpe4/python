def circle_area(radius):
    pi = 3.14
    return pi * radius ** 2
def max_of_three(a, b, c):
    return max(a, b, c)
radius = 5
area = circle_area(radius)
print(f"Площ круга с рад {radius} = {area}")

a, b, c = 12, 7, 19

maximum = max_of_three(a, b, c)
print(f"макс из чисел {a}, {b}, {c} это {maximum}")
