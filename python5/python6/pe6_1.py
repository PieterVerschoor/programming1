def seizoen(maand):
    if maand >= 3 and maand <= 6:
        print('het is lente')
    elif maand >= 6 and maand <= 9:
        print('het is zomer')
    elif maand >= 9 and maand <= 12:
        print('het is herfst')
    elif maand >= 12 and maand <= 3:
        print('het is winter')
    elif maand >= 13:
        print('Gefeliciteerd! U bent verder dan de tijd ;)')




seizoen(int(input('Wat is het maandnummer?')))