ini, fim = input().split(" ")
ini, fim = int(ini), int(fim)

if ini == fim:
    print("O JOGO DUROU 24 HORA(S)")
elif ini > fim:
    com = 24 - ini
    cont = 0
    for i in range(0, fim):
        cont += 1
    print(f"O JOGO DUROU {com + cont} HORA(S)")
else:
    temp = fim - ini
    print(f"O JOGO DUROU {fim - ini} HORA(S)")