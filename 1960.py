lis = [0, 0, 0]
pg = input()

if len(pg) == 1:
    lis[2] = int(pg)
elif len(pg) == 2:
    lis[1] = int(pg[0])
    lis[2] = int(pg[1])
elif len(pg) == 3:
    lis[0] = int(pg[0])
    lis[1] = int(pg[1])
    lis[2] = int(pg[2])

c1 = {0: "", 1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
c2 = {0: "", 1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
c3 = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}

pal = c1[lis[0]] + c2[lis[1]] + c3[lis[2]]

print(pal)