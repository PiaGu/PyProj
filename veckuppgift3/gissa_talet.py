# Slumpa ett hemligt tal


#Exempel:
#Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?
#Gissa: 40
#Nej, det är för lågt!
#Gissa: 55
#Nej, det är för högt!
#Gissa: 51
#Det är rätt!! Du gjorde det på 3 gissningar.



import random
alla_tal = []  # Lista för att lagra alla gissade tal
antal_gissningar = 0  # Variabel för att hålla summan av alla gissningar
gissning = 0
# Slumpa fram ett tal
hemligt_tal = random.randint(1, 100)
print(f"\nDet hemliga talet är  {hemligt_tal} ")

print("Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. ")
print("Kan du gissa vilket det är?")

# Samla ihop gissningarna
while True:
    user_input = input("Vilket tal gissar du på?: ")
    try:
        if user_input.isdigit():  # Kontrollera att det är en siffra
            gissning= int (user_input)
            if 1 <= gissning <= 100:
                print(f"\nGiltligt nummer! Du gissade {gissning}")
                alla_tal.append(gissning)
                if hemligt_tal == gissning:
                    print (f"Du gissade rätt! ")
                    print(f"Antal gissningar: {len(alla_tal)}")
                    break
                elif hemligt_tal != gissning:
                    alla_tal.append(gissning)
                    print(f"\nDu gissade {gissning} Det är fel, försök igen!")
                    break
            else:
                print(f"\nDu gissade {gissning} inget giltligt tal. Ska vara 1-100, Försök igen!")
                break
        else:
            print(f"\nDu gissade {user_input} Något har hänt!")
            break
    except ValueError:
        print(f"\nDu gissade {user_input}, vilket är en felaktig inmating!")