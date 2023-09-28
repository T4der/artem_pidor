import math

x = float(input("Введіть значення x: "))

x_kvad = x**2
x_cube = x**3
four_dob = 4*x_cube
thr_dob = 3*x_kvad

res = 1 - 2 * x + thr_dob - four_dob

print("Результат: " res)
