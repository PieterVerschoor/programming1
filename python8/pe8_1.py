paars = {'Boxtel', 'Best', 'Eindhoven', 'Helmond \'t hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
geel = {'Boxtel....'}

print('Beide trajecren doen de volgende station aan: {}'.format(geel.intersection(paars)))
print (''.format(geel.difference(paars)))
print ('....')