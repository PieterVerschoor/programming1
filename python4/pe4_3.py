def lang_genoeg(lengte):
    if lengte >= 120:
        print ('Je bent lang genoeg voor de attractie!')
    else:
        print ('Helaas, je bent niet lang genoeg...')

lang_genoeg(int(input('Wat is uw lengte in cm?')))