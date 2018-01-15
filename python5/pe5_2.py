a = open('kaartnummers.txt' ,'w')
a.write('325255, Jan Jansen\n334343, Erik Materus\n235434, Ali Ahson\n645345, Eva Versteeg\n534545, Jan de Wilde')
a.close()

b = open('kaartnummers.txt' , 'r')

for klantkaart in b.readlines():
    nummer = klantkaart[:6]
    naam = klantkaart[8:-2]
    print(naam,'heeft klantnummer',nummer)

lines = b.readlines()

