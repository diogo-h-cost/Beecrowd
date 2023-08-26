n = int(input())
for i in range(n):
    pal = input().upper()

    lis = list(pal)
    met = len(lis) // 2

    cop = lis[0:met]

    lis[0:met] = cop[::-1]

    cop2 = lis[met:]
    lis[met:] = cop2[::-1]

    pal = "".join(lis)
    print(pal)