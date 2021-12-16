gadgets = ["Bateria", "Portatil", 100, "Ordenador central", 310.28, "Altavoces", 27.00, "Pantalla", 1000, "Maletin electronico", "Lente de camara"]

stringList = []
numList = []

for i in gadgets:
    try:
        numList.append(float(i))
    except:
        stringList.append(i)

print(f"\n{numList}")
print(f"\n{stringList}")

stringList = sorted(stringList)
print(f"\n{stringList}")
print(f"\n{stringList[::-1]}")

numList = sorted(numList)
print(f"\n{numList}")
print(f"\n{numList[::-1]}")