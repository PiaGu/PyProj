# Balder
#För att få åka Balder på Liseberg måste man vara 130 cm lång. Skriv ett program som kan säga om man får åka!
#Fråga användaren hur lång man är (i cm)
#Skriv ut antingen "Du får åka!" eller "Du får inte åka"
#Skriv in följande värden för att testa att ditt program gjort rätt:
#121 cm (får inte åka)
#130 cm (får åka)
#155 cm (får åka)

#Diskutera:
#Varför just tre värden? För att vilkoret är endast 1
#Varför dessa värden? Ett värde på gränsen och ett över och ett under
#Skulle det vara bra att lägga till testvärdet 129 cm? Gränsvärden är alltid bra att testa.
try:
    height = int (input("Ange din längd i cm: "))

except ValueError:
    print ("Ange ett heltal")

if height >= 130:
    print(f"Du är {height} cm lång och får åka Balder")
else:
    print(f"Du är {height} cm lång och får inte åka Balder")