com = int(input())
dire = ["N", "L", "S", "O"]

while com != 0:
    pal = input()
    rot = 0

    for j in range(len(pal)):
        if pal[j] == "D":
            rot = (rot + 1) % 4

        elif pal[j] == "E":
            rot = (rot - 1) % 4

    print(dire[rot])
    com = int(input())