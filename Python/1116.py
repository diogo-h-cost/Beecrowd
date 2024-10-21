n = int(input())

for i in range(n):

    a, b = input().split(" ")
    a, b = int(a), int(b)
    
    if a < 0 or b == 0:
        print("divisao impossivel")
    else:
        div = a / b
        print(f"{div:.1f}")