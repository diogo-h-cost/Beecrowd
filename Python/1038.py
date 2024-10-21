cod, quat = input().split(" ")
cod = int(cod)
quat = int(quat)
som = 0

if cod == 1:
    som += quat * 4.00
elif cod == 2:
    som += quat * 4.50
elif cod == 3:
    som += quat * 5.00
elif cod == 4:
    som += quat * 2.00
else:
    som += quat * 1.50

print(f"Total: R$ {som:.2f}")