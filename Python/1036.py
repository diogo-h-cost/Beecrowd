from math import sqrt

a, b, c = input().split(" ")
a, b, c = float(a), float(b), float(c)

if a <= 0 or b <= 0 or c <= 0:
    print("Impossivel calcular")
else:
    delt = (b**2) - 4 * a * c
    if delt <= 0:
        print("Impossivel calcular")
    elif delt > 0:
        r1 = ((-b) + sqrt(delt)) / (2 * a)
        r2 = ((-b) - sqrt(delt)) / (2 * a)
        print(f"R1 = {r1:.5f}")
        print(f"R2 = {r2:.5f}")