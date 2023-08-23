n = int(input())

p1 = "one"
p2 = "two"

for i in range(n):
    let = input().lower()
    if len(let) == 3:

        pt = 0
        for j in range(len(let)):
            if let[j] == p1[j]:
                pt += 1

        pt2 = 0
        for k in range(len(let)):
            if let[k] == p2[k]:
                pt2 += 1

        if pt >= 2:
            print(1)
        elif pt2 >= 2:
            print(2)
            
    else:
        print(3)