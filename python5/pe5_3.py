kaartnummers = open('kaartnummers.txt', 'r')
data = kaartnummers.readlines()
g_getal = 0
lines = 0

for nummer in data:
    getal = eval(nummer[:6])
    lines = lines + 1

    if g_getal <= getal:
        g_getal = getal

print('dit is het hoogste klantnummer' , g_getal)
print('het document bestaan uit' , lines , 'regels' )
