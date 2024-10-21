while True:
    a = float(input())
    while a < 0 or a > 10:
        print("nota invalida")
        a = float(input())
    b = float(input())
    while b < 0 or b > 10:
        print("nota invalida")
        b = float(input())
    print(f"media = {((a + b) / 2):.2f}")
    print("novo calculo (1-sim 2-nao)")
    x = int(input())
    while x != 1 and x != 2:
        print("novo calculo (1-sim 2-nao)")
        x = int(input())
    if x == 2:
        break