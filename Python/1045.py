a, b, c = input().split(" ")
a, b, c = float(a), float(b), float(c)

if b > a and b > c:
    a, b, c = b, a, c
elif c > a:
    a, b, c = c, b, a

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
elif (a**2) == (b**2 + c**2):
    print("TRIANGULO RETANGULO")
elif (a**2) >= (b**2 + c**2):
    print("TRIANGULO OBTUSANGULO")
elif (a**2) <= (b**2 + c**2):
    print("TRIANGULO ACUTANGULO")

if a == b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or a == c:
    print("TRIANGULO ISOSCELES")
elif b == c:
    print("TRIANGULO ISOSCELES")