import math

a = float(input("Введіть значення a: "))

a_kvadr = a**2
a_four = a_kvadr * a_kvadr
a_visim = a_four * a_four
a_sim = a_four * a_kvadr * a

print(f"Число {a} в 7-ому степені: {a_sim}")
print(f"Число {a} в 8-ому степені: {a_visim}")