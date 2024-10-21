a, b, c = input().split(" ")
a, b, c = float(a), float(b), float(c)

a1 = (a * c) / 2
b1 = 3.14159 * (c ** 2)
c1 = ((a + b) * c) / 2
d = b ** 2
e = a * b

print(f"TRIANGULO: {a1:.3f}")
print(f"CIRCULO: {b1:.3f}")
print(f"TRAPEZIO: {c1:.3f}")
print(f"QUADRADO: {d:.3f}")
print(f"RETANGULO: {e:.3f}")