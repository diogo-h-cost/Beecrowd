l, r = input().split(" ")

while True:
    l, r = int(l), int(r)
    if l == r == 0:
        break
    print(l+r)
    l, r = input().split(" ")