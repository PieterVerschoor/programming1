def gemiddelde(x):
    words = x.split()
    average = sum(len(word) for word in words) / len(words)
    print (int(average))



gemiddelde(input('Typ een zin:'))