import math

a = float(input("Введіть довжину сторони основи піраміди: "))
h = float(input("Введіть висоту піраміди: "))

osn = a**2
bichn = 4 * (1/2) * a * h
V = (1/3) * osn * h
S = osn + bichn

print("Об'єм піраміди: " V)
print("Повна площа поверхні піраміди: " S)
