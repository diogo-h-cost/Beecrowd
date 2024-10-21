senha = 2002

while True:
    login = int(input())
    if login == senha:
        break
    else:
        print("Senha Invalida")
print("Acesso Permitido")