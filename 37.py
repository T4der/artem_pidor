a = float(input("Введіть  першу сторону :"))
print(" a =", a)
b = float(input("Введіть  другу сторону :"))
print(" b =", b)
c = float(input("Введіть  третю сторону :"))
print(" z =", c)

if a+b>c or a+c>b or b+c>a:
    print("Це трикутник")
elif a+b<c:
    print("Це не є трикутник")

if a ** 2 + b ** 2 == c ** 2 :
    print("Трикутник прямокутний")
elif a==b or b==c or c==a :
    print("це рівнобедренний трикутник")
elif a ** 2 + b ** 2 > c ** 2 or a ** 2 + c ** 2 > b ** 2 or b ** 2 + c ** 2 > a ** 2:
    print("трикутник гострокутній")
elif a ** 2 + b ** 2 < c ** 2 or a ** 2 + c ** 2 < b ** 2 or b ** 2 + c ** 2 < a ** 2:
    print("трикутник тупокутній")