menyu = {
        'osh':30000,
        "shashlik":22000,
        "manti": 5000,
        "non":2000,
        'choy':5000,
        'cola':15000,
        'fanta':15000,
        'sok':13000
        }

print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menyu:
        print(f"{buyurtma.title()} {menyu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")