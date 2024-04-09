while True:
    pos = input().split(" ")
    pos = list(map(int, pos))

    if sum(pos) == 0:
        break

    if pos[0] == pos[2] and pos[1] == pos[3]:
        print(0)
    elif (pos[0] == pos[2] or pos[1] == pos[3]) or (abs(pos[0] - pos[2]) == abs(pos[1] - pos[3])):
        print(1)
    else:
        print(2)