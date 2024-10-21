vet = [0] * 10
for i in range(10):
    val = int(input())
    if val > 0:
        vet[i] = val
    else:
        vet[i] = 1
for i in range(10):
    print(f"X[{i}] = {vet[i]}")