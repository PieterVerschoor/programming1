def inlezen_beginstation(station):
    while True:
        print(station)
        station = input('beginstation')
        if station in stations:
            return station

def inlezen_eindstation(stations, beginstation):
    index_begin_station = stations.index(beginstation)
    while True:
        station = input('eindstation')
        if station in stations:
            index_eind_station = stations.index(station)
            if index_eind_station > index_begin_station:
                return station

def omroepen_reis(station, beginstation, eindstation):
    index_begin = stations.index(beginstation) + 1
    begin = 'Het beginstation is {} en heeft als index {}'.format(beginstation, str(index_begin))
    index_eind = stations.index(eindstation) + 1
    eind = 'Het eindstation is {} en heeft als index {}'.format(eindstation, str(index_eind))

    print(begin)
    print(eind)
    afstand = index_eind - index_begin
    print('Stand is {}'.format(str(afstand)))
    if afstand > 1:
     for index in range(index_begin + 0, index_eind):
        print(' - ' + stations[index])

stations = ['Schagen','Heerhugowaard','Alkmaar','Castricum','Zaandam','Amsterdam Sloterdijk','Amsterdam Centraal','Amsterdam Amstel','Utrecht Centraal',"’s-Hertogenbosch",'Eindhoven','Weert',
'Roermond','Sittard','Maastricht']
begin_station = inlezen_beginstation(stations)
eind_station = inlezen_eindstation(stations, begin_station)
omroepen_reis(stations, begin_station, eind_station)