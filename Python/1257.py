def posic_let(let):
    return ord(let) - ord('A')

casos = int(input())
for i in range(casos):
    soma = 0
    lin = int(input())
    for j in range(lin):
        let = input().upper()
        for k in range(len(let)):
            alf = posic_let(let[k])
            soma += (alf + j + k)
    print(soma)