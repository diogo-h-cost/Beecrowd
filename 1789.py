while True:
    try:
        n = int(input())
        vel = input().split(" ")
        lis = []
        for i in vel:
            lis.append(int(i))
        if max(lis) < 10:
            print(1)
        elif max(lis) < 20:
            print(2)
        else:
            print(3)
    except EOFError:
        break