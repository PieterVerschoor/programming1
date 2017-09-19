a = int(input('Vul je leeftijd in:'))
b = str(input('Ben je in het bezit van een geldig Nederlands paspoort? Ja/Nee:'))
if a < 18 or b == 'Nee':
    print ('Je mag helaas niet stemmen...')
else:
    print ('Je mag stemmen!')