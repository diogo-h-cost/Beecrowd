while True:
    n = int(input())
    pa = pb = 0
    if n == 0:
        break
    for i in range(n):
        a, b = input().split(" ")
        a, b = int(a), int(b)
        if a > b:
            pa += 1
        elif b > a:
            pb += 1
    print(f"{pa} {pb}")