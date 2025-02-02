import random

# Slumpa fram ett tal
hemligt_tal = random.randint(1, 100)
alla_tal = []  # Lista för att spara gissningar

print("\nVälkommen till Gissa talet!")
print("Jag tänker på ett tal mellan 1 och 100.")

while True:
    user_input = input("\nVilket tal gissar du på?: ")

    if user_input.isdigit():  # Kontrollera att input bara innehåller siffror
        gissning = int(user_input)

        if 1 <= gissning <= 100:  # Kontrollera att talet är inom intervallet
            alla_tal.append(gissning)  # Spara gissningen

            if gissning == hemligt_tal:
                print(f"\n Du gissade rätt! ")
                print(f"Det hemliga talet var {hemligt_tal}.")
                print(f"Antal gissningar: {len(alla_tal)}")
                break  # Avsluta spelet

            else:
                print(f"\nDu gissade {gissning}. Det är fel, försök igen!")

                # Om gissningen är inom 5 tal från det hemliga talet
                if (hemligt_tal - 5) <= gissning <= (hemligt_tal + 5):
                    print(" Nu börjar det brännas! ")
        else:
            print(f"\n{gissning} är utanför intervallet 1-100. Försök igen!")
    else:
        print("\nFelaktig inmatning! Ange ett heltal mellan 1 och 100.")
