x = [1,2,3,4,5,6,7,8,9,10]

for item in x:
    print(item + 10) #Erhöht die Liste um 10, aber hier bleibt x mit einer Liste von 10
    x[item] = input("Gib etwas ein: ") #Ich kann nun so lang die Liste ist etwas eingeben

y = "garten"

for i in x:
    print(i)
"""
                Ausgabe:
                        g
                        a
                        r
                        t
                        e
                        n
"""

for z in range(10):
    print(z)
else:
    print("Jetzt kommt die Else ausgabe")
    #Die Forschleife wird so lange ausgeführt bis die range erreicht ist, dann kommt else