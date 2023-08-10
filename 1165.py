n = int(input())

for i in range(n):
    t = int(input())
    pv = 0
    for j in range(1, t+1):
        if t % j == 0:
            pv += 1
    if pv == 2:
        print(f"{t} eh primo")
    else:
        print(f"{t} nao eh primo")