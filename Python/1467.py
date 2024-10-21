while True:
    try:
        a, b, c = input().split(" ")
        a, b, c = int(a), int(b), int(c)
        entr = [0, 1]
        if a and b and c not in entr:
            break
        if a == b == c:
            print("*")
        elif a == b:
            print("C")
        elif a == c:
            print("B")
        elif c == b:
            print("A")
    except EOFError:
        break