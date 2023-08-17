n = int(input())

while n != 0:
    num = input().split(" ")
    mar = joa = 0
    for i in num:
        if i == "0":
            mar += 1
        else:
            joa += 1
    print(f"Mary won {mar} times and John won {joa} times")
    n = int(input())