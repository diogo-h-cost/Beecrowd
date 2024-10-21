a, b, c = input().split(" ")
a, b, c = float(a), float(b), float(c)

l = [a, b, c]
list = [a, b, c]
men1 = min(l)
l.remove(min(l))

if (men1 + min(l)) > max(l):
    print(f"Perimetro = {sum(list):.1f}")
else:
    print(f"Area = {((a+b) * c / 2):.1f}")