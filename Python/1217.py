n = int(input())

kg = []
gast = 0

for i in range(n):
    pre = float(input())
    nom = input().split(" ")
    kg.append(len(nom))
    gast += pre

for i in range(len(kg)):
    print(f"day {i+1}: {kg[i]} kg")

print(f"{sum(kg)/n:.2f} kg by day")
print(f"R$ {gast/n:.2f} by day")