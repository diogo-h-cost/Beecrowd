x = int(input())
y = int(input())

if x > y:
    x, y = y, x

l = []
for i in range(x, y):
    if i % 2 != 0:
        if i != x and i != y:
            l.append(i)

print(f"{sum(l)}")