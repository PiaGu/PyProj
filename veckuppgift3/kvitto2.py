#Denna fungerar men kan förbättras

alla_kostnader = []  # Lista för att lagra alla kostnader
total_kostnad = 0.0  # Variabel för att hålla summan av alla kostnader (startvärde som float)

print("Välkommen till Kvittokompis!")
print("Skriv in dina kostnader som decimaltal. Skriv 'quit' för att avsluta.")

# Först loopen, samla ihop kostnader, loopa tills användaren vill avsluta
while True:
    user_input = input("Ange en kostnad (eller 'quit' för att avsluta): ")

    if user_input.lower() == "quit":  # Kontrollera om användaren vill avsluta
        break  # Avsluta loopen

    try:
        kostnad = float(user_input)  # Försök att omvandla inmatningen till ett flyttal
        if kostnad < 0:  # Kolla att kostnaden är positiv
            print("Kostnaden kan inte vara negativ. Försök igen.")
        else:
            alla_kostnader.append(kostnad)  # Lägg till kostnaden i listan
            total_kostnad += kostnad  # Lägg till kostnaden till den totala summan
            print(f"Kostnaden {kostnad:.2f} har lagts till. Nuvarande totalsumma: {total_kostnad:.2f} kr")
    except ValueError:
        print("Felaktig inmatning. Ange ett decimaltal eller 'quit' för att avsluta.")

# Fråga om dricks och räkna ut
while True: # Loopa tills användaren ger ett tal eller bara enter
    user_input3 = input("Ange i ett heltal hur mycket dricks som ska läggas på: ")
    try:
        if user_input3 == "":
            tip = 10
            break

        # Kontrollera att inmating är en siffra och dricksen är större än 0
        elif user_input3.isdigit() and int(user_input3) > 0:
            tip = int (user_input3)
            break  # Avsluta loopen

        else:
            print("Felaktig inmatning Ange ett tal.")  # Om användaren matar ej tal, ge felmeddelande
    except ValueError:
        print("Felaktig inmatning. Ange ett tal.") # Om användaren matar ej tal, ge felmeddelande

tip_cost = (tip/100) * total_kostnad
print(f"{tip} procents dricks av {total_kostnad} kr blir {tip_cost} kronor")
total_kostnad = total_kostnad + tip_cost

# Visa totalen efter att användaren har avslutat kostnadsinmatningen
print(f"Den totala kostnaden är: {total_kostnad:.2f} kr")

while True: # Loopa tills användaren ger ett tal
    user_input2 = input("Hur många personer är ni? ")
    try:
        number_of_people = int (user_input2)  # Försök att omvandla inmatningen till en int
        if number_of_people <= 0:  # Kontrollera att antalet personer är större än 0
            print("Antalet personer måste vara ett positivt heltal. Försök igen.")
        else:
            cost_per_person = total_kostnad/number_of_people # Räkna ut kostnad per person
            print(f"Det blir {cost_per_person:.2f} kr per person")
            break # Avsluta loopen
    except ValueError:
        print("Felaktig inmatning. Ange hur många ni är med ett tal.") # Om användaren matar ej tal, ge felmeddelande