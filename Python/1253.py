vez = int(input())
for i in range(vez):
    pal = input()
    pos = int(input())
    let = list(pal)
    for j in range(len(let)):
        nov = ord(let[j]) - pos
        if nov < 65:
            nov += 26
        elif nov > 90:
            nov -= 26
        let[j] = chr(nov)
    print("".join(let))