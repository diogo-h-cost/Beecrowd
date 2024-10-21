sal = float(input())

if sal <= 400.00:
    reaj = (15 * sal) / 100
    per = "15 %"
elif sal <= 800.00:
    reaj = (12 * sal) / 100
    per = "12 %"
elif sal <= 1200.00:
    reaj = (10 * sal) / 100
    per = "10 %"
elif sal <= 2000.00:
    reaj = (7 * sal) / 100
    per = "7 %"
else:
    reaj = (4 * sal) / 100
    per = "4 %"

print(f"Novo salario: {sal+reaj:.2f}")
print(f"Reajuste ganho: {reaj:.2f}")
print(f"Em percentual: {per}")