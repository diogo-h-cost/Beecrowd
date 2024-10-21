grit = pont = 0
while grit != 3:
    ent = input()
    if ent == "caw caw":
        print(pont)
        pont = 0
        grit += 1
    else:
        olh = list(ent)
        for i in range(len(ent)):
            if olh[0] == "*" and i == 0:
                pont += 4
            elif olh[1] == "*" and i == 1:
                pont += 2
            elif olh[2] == "*" and i == 2:
                pont += 1