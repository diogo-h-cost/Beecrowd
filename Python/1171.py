n = int(input())

lis = []
for i in range(n):
    num = int(input())
    lis.append(num)

lis.sort()

dic = {}
for j in lis:
    dic[j] = dic.get(j, 0) + 1
for a, b in dic.items():
    print(f"{a} aparece {b} vez(es)")