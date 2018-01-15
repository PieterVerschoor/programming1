temp_celcius = eval(input("Hoeveel graden celcius is het ?"))

def convert(celcius):
    temp_farhenheit = celcius * 1.8 + 32
    return temp_farhenheit

temp_farhenheit = convert(temp_celcius)
print(temp_farhenheit, "graden farhenheit")



def table():
    c_tabel = range(-30, 50, 10)
    print('{:>5}\t{:>5}'.format('  F  ', '  C  '))
    for c in c_tabel:
        f = convert(c)
        fancy_tabel = '{:>5} {:>5}'.format(f , c)
        print(fancy_tabel)
table()

