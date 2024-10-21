ida = int(input())

dat = [365, 30, 1]
seq = ["ano(s)", "mes(es)", "dia(s)"]

for i in range(3):
    temp = ida // dat[i]
    print(f"{temp} {seq[i]}")
    ida %= dat[i]