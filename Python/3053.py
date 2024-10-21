mov = int(input())
moe = input()

a = b = c = 0

if moe == "A":
    a = 1
elif moe == "B":
    b = 1
elif moe == "C":
    c = 1

for i in range(mov):
    n = int(input())
    if n == 1:
        a, b = b, a
    elif n == 2:
        b, c = c, b
    elif n == 3:
        a, c = c, a
        
if a > 0:
    print("A")
elif b > 0:
    print("B")
elif c > 0:
    print("C")