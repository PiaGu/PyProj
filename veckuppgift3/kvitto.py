#Gör ett program som upprepade gånger ber användaren skriva in ett tal. När man skriver in strängen "quit" eller "avsluta" ska programmet ska det räkna ut summan av talen. Exempel:
#Välkommen till Kvittokompis! Avsluta genom att skriva: quit
#Skriv in ett belopp: 25
#Skriv in ett belopp: 50
#Skriv in ett belopp: quit
#Det blir 75 kr totalt. Välkommen åter!
#Version 2: programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.
#Hur många är ni? 3
#Det blir 75 kr totalt, alltså 25.0 kr per person. Välkommen åter!
#Version 3: programmet ska fråga hur många procent dricks man vill lägga på. Om användaren inte skriver något (tom sträng) ska programmet använda 10% som standardinställning.
#Nice to have: prova att använda try+except eller isdigit för att hantera de fall när användaren skriver ett felaktigt värde. Python Try Except , isdigit | StackOverflow
#("Nice to have" handlar om funktionalitet som inte är nödvändig, men som är bra att ha. Gå gärna vidare till nästa uppgift och återvänd till den här om du vill lära dig mer.)

#Testa programmet med följande inputs:
#Version 1:
#100
#10, 20, 15
#Version 2:
#100, 1 person
#100, 2 personer
#10, 10, 40 personer
#30, 20, 30, 1 person
#Lägg till egna testfall för dricksen.

#alla_kostnader: list[int] = []

alla_kostnader = []
while True:
    user_input = (input("Välkommen till Kvittokompis! Skriv in dina kostnader. (Avsluta genom att skriva quit.) :  "))
    
    if user_input.lower() == "quit":
        print(f"Du angav {user_input} avslutar")
        print(f"Den totala kostnaden är: {total_kostnad}")
        break
    elif user_input.isdigit():  #Kontrollera att inmatningen är en siffra
        alla_kostnader.append(int(user_input)) # Lägg till kostnaden i listan
        total_kostnad = 0  # Startvärde för totalsumman
        for i in alla_kostnader:
            total_kostnad += i

        print(f"Den totala kostnaden är: {total_kostnad}")

    else:
        print("Nu är du i else satsen")     # om man matar in annat än quit eller positv heltalsiffra,  kasta försök igen
        
#    elif user_input == "avsluta":
#        total_kostnad = 0  # Startvärde för summan
#        for i in alla_kostnader:
#            total_kostnad += i

#        print(f"Den totala kostnaden är: {total_kostnad}")

#

 #   alla_kostnader: list[int] = []kost = int(user_input)

  #  print(f"{alla_kostnader}")

#numbers = []  # Lista för att lagra siffror

#while True:
#    user_input = input("Ange ett nummer (eller något annat för att avsluta): ")

 #   if user_input.isdigit():  # Kontrollera om inmatningen är en siffra
  #      numbers.append(int(user_input))  # Lägg till siffran i listan


#print(f"Listan med siffror: {numbers}")

#print("inte ett nummer")
#try:
 #   number = float(user_input)  # Försök att konvertera till ett flyttal
  #  print(f"Inmatningen är en siffra: {number}")
#except ValueError:
#    print("Inmatningen är en sträng eller ogiltig siffra!")





#print(f"kostnaden var: {kostnad}")
#print(type(kostnad))
#alla_kostnader.append(kostnad)
#print(type(alla_kostnader))
#print(f"Kostnaden är: {alla_kostnader}")
