import math

x = float(input("Введіть значення x: "))
y = float(input("Введіть значення y: "))

res = x - (x**3) / (math.factorial(3)) +  (y**5) / (math.factorial(5))