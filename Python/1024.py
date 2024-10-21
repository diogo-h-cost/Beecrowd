n = int(input())

for i in range(n):
    let = input()
    lis = list(let)

    for j in range(len(lis)):
        if lis[j].isalpha():
            x = ord(lis[j]) + 3
            lis[j] = chr(x)

    lista = lis[::-1]
    meta = len(lista) // 2

    for t in range(meta, len(lista)):
        a = ord(lista[t]) - 1
        lista[t] = chr(a)

    pal = "".join(lista)
    print(pal)