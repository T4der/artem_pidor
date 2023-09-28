import math

x = float(input("Введіть значення x: "))
y = float(input("Введіть значення y: "))
z = float(input("Введіть значення z: "))

res = (3 + math.exp(y - 1)) / (1 + x ** 2 * abs(y - math.tan(z)))

print("Результат: " res)
