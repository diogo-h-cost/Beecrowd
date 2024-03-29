val = float(input())

din = val

vez = [0] * 12

name1 = ["100", "50", "20", "10", "5", "2"]
name2 = ["1.00", "0.50", "0.25", "0.10", "0.05", "0.01"]
notas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

din *= 100

for i in range(12):
    if din >= (notas[i] * 100):
        vez[i] += int(din / (notas[i] * 100))
        din -= vez[i] * (notas[i] * 100)

print("NOTAS:")
for i in range(6):
    print(f"{vez[i]} nota(s) de R$ {name1[i]}.00")

print("MOEDAS:")
for i in range(6):
    print(f"{vez[i + 6]} moeda(s) de R$ {name2[i]}")