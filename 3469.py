num = int(input())
seq = input().split(" ")
lis = [int(i) for i in seq]
lis.sort()
meio = len(lis) // 2
if len(lis) % 2 == 0:
    m1 = lis[meio - 1]
    m2 = lis[meio]
    print(int((m1 + m2) / 2))
else:
    print(lis[int(meio)])