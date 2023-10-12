#a
a = float(input("Введіть дійсне число а :"))
print(" a =", a)
if a<=2:
    f=a**2 + 4 * a +5
else:

    f =1/ (a**2 + 4 * a +5)
    print(f'f({a}) = {f}')

#b
a = float(input("Введіть дійсне число а :"))
print(" a =", a)
if a<=0:
    f=0
elif a>0 and a<=1:
    f = a ** 2 - a
elif a>=1:
    f=a ** 2 - a * 0.5
    print(f'f({a}) = {f}')





