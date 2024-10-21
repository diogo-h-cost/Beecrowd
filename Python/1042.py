n1, n2, n3 = input().split(" ")
n1, n2, n3 = int(n1), int(n2), int(n3)

l2 = [n1, n2, n3]
l1 = [n1, n2, n3]

l1.sort()

for i in range(3):
    print(l1[i])

print()

for i in range(3):
    print(l2[i])