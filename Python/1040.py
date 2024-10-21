n1, n2, n3, n4 = input().split(" ")
n1, n2, n3, n4 = float(n1), float(n2), float(n3), float(n4)

med = ((((n1 * 2) + n2 * 3) + n3 * 4) + n4) / 10.0
print(f"Media: {med:.1f}")

if med >= 7.0:
    print("Aluno aprovado.")
elif med < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    n5 = float(input())
    print(f"Nota do exame: {n5}")
    media = (med + n5) / 2
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media}")