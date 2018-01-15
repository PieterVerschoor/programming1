def gemiddelde(zin):
    total = 0
    avg = zin.split()
    for i in avg:
        total += len(i)
    ave_size = float(total) / float(len(avg))
    print(ave_size)

gemiddelde(input('Voer een willekeurige zin in: '))
