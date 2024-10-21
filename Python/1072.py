n = int(input())

den = fora = 0
for i in range(n):
    num = int(input())
    if num >= 10 and num <= 20:
        den += 1
    else:
        fora += 1

print(f"{den} in")
print(f"{fora} out")