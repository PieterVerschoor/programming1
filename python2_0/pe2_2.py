cijferICOR = 6.5
cijferPROG = 7.5
cijferCSN = 7.0
totaal = ((cijferICOR)+(cijferPROG)+(cijferCSN))
gemiddelde = (totaal)/3
beloning = (totaal)*30
overzicht = 'Mijn cijfers (gemiddeld een {}) leveren een beloning van €{} op!'.format(gemiddelde, beloning)

print (overzicht)