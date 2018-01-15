def hardlooptijd():
    naam = input('wat is de hardloopers naam ?')
    import time
    a = open('hardlopers.txt' , 'a')
    tijd = time.strftime('%A %d %b %Y, %I:%M:%S')
    tijd_naam = tijd + naam + '\n'
    a.write(tijd_naam)
    a.close()

hardlooptijd()