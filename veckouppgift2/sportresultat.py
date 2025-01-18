#3 Sportresultat
#Tottenham spelar mot Liverpool i Champions League.
# Skriv ett program som frågar användaren hur många mål respektive lag gjorde,
# och talar om vilket lag som vann.
#Exempel på output:
#Matchen är över, nu ska vi räkna ut resultatet!
#3Hur många mål gjorde Tottenham? 2
#Hur många mål gjorde Liverpool? 1
#Tottenham vann!
##ersion 2: programmet ska tala om ifall det blev oavgjort.

#Version 3: nu ska programmet tala om hur många mål mer laget vann med. Exempel:
#Tottenham vann med 1 mål!

#Eftersom det finns tre möjliga utfall (lag 1 vinst, lag 2 vinst, oavgjort) behöver du minst tre testfall. Hitta på värden som du kan använda för att testa alla möjliga utfall.

try:
    liverpool_goal = int (input("Hur många mål gjorde Liverpool? "))
    tottenham_goal = int (input("Hur många mål gjorde Tottenham? "))
except ValueError:
    print("Ange antal mål som ett heltal")

if liverpool_goal > tottenham_goal:
    print (f"Liverpool vann! Liverpool gjorde {liverpool_goal} mål och Tottenham gjorde {tottenham_goal} mål")
    more_goal = liverpool_goal - tottenham_goal
    print(f"Liverpool gjorde {more_goal} fler mål")

elif liverpool_goal < tottenham_goal:
    print (f"Tottenham vann! Tottenham gjorde {tottenham_goal} mål och Liverpool gjorde {liverpool_goal} mål")
    more_goal = tottenham_goal - liverpool_goal
    print(f"tottenham gjorde {more_goal} fler mål")

else:
    print(f"Det blev oavgjort, Tottenham gjorde {tottenham_goal} mål och Liverpool gjorde {liverpool_goal} mål")




