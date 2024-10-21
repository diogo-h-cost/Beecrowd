vez = int(input())

for i in range(vez):
    lista = [2, 5, 5, 4, 5, 6, 3, 7, 6, 6]
    nume = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = input()
    cont = 0
    for j in num:
        if int(j) in nume:
            cont += lista[int(j)-1]
    print(f"{cont} leds")