num = int(input())

tab = {61: "Brasilia", 71: "Salvador", 11: "Sao Paulo", 21: "Rio de Janeiro",
       32: "Juiz de Fora", 19: "Campinas", 27: "Vitoria", 31: "Belo Horizonte"}

if num in tab:
    print(tab[num])
else:
    print("DDD nao cadastrado")