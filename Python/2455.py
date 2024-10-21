p1, c1, p2, c2 = input().split(" ")
p1, c1, p2, c2 = int(p1), int(c1), int(p2), int(c2)

som1 = p1 * c1
som2 = p2 * c2

if som1 == som2:
    print("0")
elif som1 > som2:
    print("-1")
else:
    print("1")