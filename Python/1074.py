n = int(input())

for i in range(n):
    n1 = int(input())
    if n1 == 0:
        print("NULL")
    elif n1 % 2 == 0:
        if n1 > 0:
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    else:
        if n1 > 0:
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")