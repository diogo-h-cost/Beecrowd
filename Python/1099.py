n = int(input())

for i in range(n):
    x, y = input().split(" ")
    x, y = int(x), int(y)

    if y < x:
        x, y = y, x

    soma = 0
    for j in range(x+1, y):
        if j % 2 != 0:
            soma += j
            
    print(soma)