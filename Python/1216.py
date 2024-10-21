lista = []

while True:
    try:
        nome = input()
        dis = int(input())
        lista.append(dis)
    except EOFError:
        break
    
print(f"{sum(lista)/len(lista):.1f}")