lis = []
while True:
    x = int(input())
    if x < 0:
        break
    lis.append(x)
print(f"{sum(lis) / len(lis):.2f}")