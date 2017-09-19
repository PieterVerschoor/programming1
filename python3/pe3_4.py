week = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag']
for x in week:
    print (x[:2])


getallen = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for y in getallen:
    if (y%2==0):
        print (y)

s = 'Guido van Rossum heeft programmeertaal Python bedacht.'
for q in s:
    if (q in ('euioa')):
        print (q)