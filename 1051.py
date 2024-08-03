sal = float(input())
imp = 0
if sal > 0.00 and sal < 2_000.01:
    print("Isento")
else:
    if sal > 4_500.00:
        imp += (sal - 4_500) * 0.28
        sal = 4_500
    if sal > 3_000.00:
        imp += (sal - 3_000) * 0.18
        sal = 3_000
    if sal > 2_000.00:
        imp += (sal - 2_000) * 0.08
    print(f"R$ {imp:.2f}")