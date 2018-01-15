lijst = eval(input('Geef een lijst met minimaal 10 strubgs: '))

nieuwelijst = []
for woord in lijst:
    if len(woord) >= 4:
        nieuwelijst.append(woord)

    print(nieuwelijst)


#"boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"