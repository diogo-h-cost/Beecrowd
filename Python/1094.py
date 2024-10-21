ratos = coelhos = sapos = 0

qt = int(input())
for i in range(qt):
    n, t = input().split(" ")
    n, t = int(n), str(t).upper()
    if t == "R":
        ratos += n
    elif t == "C":
        coelhos += n
    elif t == "S":
        sapos += n

tot = ratos+coelhos+sapos

print(f"Total: {tot} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {coelhos / tot * 100:.2f} %")
print(f"Percentual de ratos: {ratos / tot * 100:.2f} %")
print(f"Percentual de sapos: {sapos / tot * 100:.2f} %")