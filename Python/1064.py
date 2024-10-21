posi = soma = 0

for i in range(6):
    n = float(input())
    if n > 0:
        posi += 1
        soma += n

print(f"{posi} valores positivos")
print(f"{soma/posi:.1f}")