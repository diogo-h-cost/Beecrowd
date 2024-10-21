x = int(input())
l = [100, 50, 20, 10, 5, 2, 1]

print(x)
for i in range(len(l)):
    cont = x // l[i]
    x = x % l[i]
    print(f"{cont} nota(s) de R$ {l[i]},00")