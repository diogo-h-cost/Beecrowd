dic = {"zero": "0", "um": "1", "dois": "2", "tres": "3", "quatro": "4", "cinco": "5", "seis": "6", "sete": "7", "oito": "8", "nove": "9", "dez": "10"}

n = input().lower()
if n in dic.values():
    for c, v in dic.items():
        if v == n:
            print(c)
else:
    print(dic[n])