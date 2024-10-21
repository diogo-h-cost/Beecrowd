posmaior = 0
maior = 0

for i in range(1, 101):
    num = int(input())
    if num > maior:
        maior = num
        posmaior = i

print(maior)
print(posmaior)