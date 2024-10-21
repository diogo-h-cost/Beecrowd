a, b = input().split(" ")
a, b = int(a), int(b)

if b > a:
    a, b = b, a

if a % b == 0:
   print("Sao Multiplos")
else:
    print("Nao sao Multiplos")