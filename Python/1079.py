n = int(input())

for i in range(n):

    a, b, c = input().split(" ")
    a, b, c = float(a), float(b), float(c)

    med = (((a * 2) + b * 3) + c * 5) / 10
    
    print(f"{med:.1f}")   