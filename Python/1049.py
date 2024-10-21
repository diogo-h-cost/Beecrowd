l1 = input().lower()
l2 = input().lower()
l3 = input().lower()

if l1 == "vertebrado":
    if l2 == "ave":
        if l3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if l3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if l2 == "inseto":
        if l3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if l3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")