c2 = 1

for i in range(0, 5):
    c1 = 8
    for j in range(0, 3):
        c1 -= 1
        print(f"I={c2} J={c1}")
    c2 += 2