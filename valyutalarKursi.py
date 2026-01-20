import os
os.system("cls")

import requests as rq

link = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'

data = rq.get(link).json()

print("Valyutalar:")

for i in range(len(data)):
    print(f" {i+1}.  1 {data[i]['CcyNm_UZ']} : {data[i]['Rate']} so'm")
    

a = int(input("Valyuta tanlang: "))
for i in range(len(data)):
    if a == i+1:
        print(f"1. {data[i]['Ccy']} -> SUM\n2. SUM -> {data[i]['Ccy']}")
        b = int(input("Tanlang: "))
        if b==1:
            c = int(input(f"Qancha {data[i]["Ccy"]}: "))
            d = float( data[i]['Rate'])
            total = c * d
            print(f"Natija: {total:.2f}")
        elif b==2:
            c=float(input("Qancha SUM:"))
            d = float( data[i]['Rate'])
            total = c/d
            print(f"Natija: {total:.2f}")
        else:
            print("Bunday tanlov yo'q!")
    else:
        print("Bunday valyuta mavjud emas!")
        break