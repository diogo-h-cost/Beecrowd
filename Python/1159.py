while True:

    n = int(input())
    
    if n == 0:
        break
    else:
        par = soma = 0
        i = n
        while par != 5:
            if i % 2 == 0:
                par += 1
                soma += i
            i += 1
        print(soma)