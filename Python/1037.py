val = float(input())

inter = ("[0,25]", "(25,50]", "(50, 75]", "(75,100]")
lis = [0, 25, 25, 50, 50, 75, 75, 100]

cont = 0
for i in range(0, 7, 2):
    if val >= lis[i] and val <= lis[i+1] :
        print(f"Intervalo {inter[cont]}")
        break
    elif val < 0 or val > 100:
        print("Fora de intervalo")
        break
    else:
        cont += 1