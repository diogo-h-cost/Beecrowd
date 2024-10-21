dia = int(input())

menb = {1: "Rolien", 2: "Naej", 3: "Elehcim", 4: "Odranoel"}

for i in range(dia):
    cas = int(input())

    for j in range(cas):
        fed = int(input())
        
        if fed in menb.keys():
            print(menb[fed])