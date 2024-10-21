x = int(input())

hor = x // 3600
min = (x % 3600) // 60
seg = ((x % 3600) % 60) // 1

print(f"{hor}:{min}:{seg}")