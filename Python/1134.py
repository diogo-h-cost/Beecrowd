al = ga = die = 0

while True:
    comb = int(input())
    if comb == 4:
        break
    elif comb == 1:
        al += 1
    elif comb == 2:
        ga += 1
    elif comb == 3:
        die += 1
        
print(f"MUITO OBRIGADO\n"
      f"Alcool: {al}\n"
      f"Gasolina: {ga}\n"
      f"Diesel: {die}")