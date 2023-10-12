x = float(input("веддіть  дійсне число x :"))
print(" x =", x)
y = float(input("веддіть  дійсне число y :"))
print(" y =", y)
if x>y:
    z=x-y
elif x<=y:
    z=y-x+1
    print(f'z({x,y}) = {z}')

