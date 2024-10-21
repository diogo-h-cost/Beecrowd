n = int(input())

x = 1
for i in range(n):
    while True:
        if x % 4 == 0:
            print("PUM")
            break
        print(x, end=" ")
        x += 1
    x += 1