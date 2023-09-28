import math

a = float(input("Введіть довжину однієї сторони паралелограма: "))
b = float(input("Введіть довжину іншої сторони паралелограма: "))
c = float(input("Введіть гострий кут між сторонами у градусах: "))

kyt = math.radians(c)
per = 2 * (a + b)
height = a * math.sin(kyt)
area = a * height

print("Периметр паралелограма: " per)
print("Площа паралелограма: " area)
