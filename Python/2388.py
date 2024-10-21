lista = []

n = int(input())

for i in range(n):
    t, v = input().split(" ")
    t, v = int(t), int(v)
    lista.append(t*v)

print(sum(lista))