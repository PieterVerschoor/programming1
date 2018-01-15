invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lijst = invoer.split('-')
nieuwe_lijst = []
for cijfer in lijst:
    nummer = int(cijfer)
    nieuwe_lijst.append(nummer)


max = max(nieuwe_lijst)
min = min(nieuwe_lijst)
s
gesorteerd = nieuwe_lijst.sort()
aantal = len(nieuwe_lijst)

som = sum(nieuwe_lijst)
gemiddelde = som / aantal

print('het grootste getal is ',max)
print('het kleinste getal is ' ,min)
print('gesorteerd van klein naar groot is ' ,gesorteerd)
print('de lengte van de lijst is ',aantal)
print('het totaal van de getallen is ' ,som)
print('en het gemiddelde van alle getallen is ',gemiddelde)