print (0 == (1 == 2))
print (2 + (3 == 4) + 5 == 7)
print ((1 < -1) == (3 > 4))

a = float(input('Wat verdien je per uur a sah?:'))
b = int(input('Hoeveel uur heb je gewerkt?:'))
c = ((a)*(b))
d = '{} uur levert je €{} op, misschien moet je ander werk zoeken.'.format(b, c)
print (d)