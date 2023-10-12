x = float(input(" Введіть першу координату :"))
print(" x =", x)
y = float(input("Введіть другу координату :"))
print(" y =", y)
if x > y:
    x /= 2
    y += 7
    print('х =', x)
    print('y =', y)
if x < y:
    y /= 2
    x += 7
    print('х =', x)
    print('y =', y)

