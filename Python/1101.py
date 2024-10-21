while True:

    m, n = input().split(" ")
    m, n = int(m), int(n)

    if m <= 0 or n <= 0:
        break

    if n < m:
        m, n = n, m

    soma = 0
    for i in range(m, n+1):
        soma += i
        print(i, end=" ")
        
    print(f"Sum={soma}")