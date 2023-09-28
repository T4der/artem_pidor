import math

a = float(input("Введіть довжину сторони куба: "))

r_in = a / 2
r_out = (a * math.sqrt(3)) / 2

V_in = (4/3) * math.pi * (r_in**3)
V_out = (4/3) * math.pi * (r_out**3)

S_in = 4 * math.pi * (r_in**2)
S_out = 4 * math.pi * (r_out**2)

print("Об'єм вписаної сфери: " V_in)
print("Об'єм описаної сфери: " V_out)
print("Площа поверхні вписаної сфери: " S_in)
print("Площа поверхні описаної сфери: " S_out)
