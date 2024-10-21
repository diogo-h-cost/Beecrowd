par = imp = pos = neg = 0

for i in range(5):
    n = int(input())
    if n % 2 == 0:
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1
        par += 1
    else:
        if n > 0:
            pos += 1
        else:
            neg += 1
        imp += 1

print(f"{par} valor(es) par(es)")
print(f"{imp} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{neg} valor(es) negativo(s)")