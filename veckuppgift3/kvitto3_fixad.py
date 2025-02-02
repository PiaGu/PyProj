alla_kostnader = []  # Lista för att lagra alla kostnader
total_kostnad = 0.0  # Variabel för att hålla summan av alla kostnader

print("Välkommen till Kvittokompis!")
print("Skriv in dina kostnader som decimaltal. Skriv 'quit' för att avsluta.\n")

# Samla ihop kostnader
while True:
    user_input = input("Ange en kostnad (eller 'quit' för att avsluta): ")
    if user_input.lower() == "quit":  # Kontrollera om användaren vill avsluta
        print("\nDu avslutade inmatningen.")
        print(f"Totalt antal kostnader: {len(alla_kostnader)}")
        print(f"Den totala kostnaden utan dricks är: {total_kostnad:.2f} kr")
        break  # Avsluta loopen
    try:
        kostnad = float(user_input)  # Omvandla till float
        if kostnad < 0:
            print("Kostnaden kan inte vara negativ. Försök igen.")
        else:
            alla_kostnader.append(kostnad)
            total_kostnad += kostnad
            print(f"Kostnaden {kostnad:.2f} har lagts till. Nuvarande totalsumma: {total_kostnad:.2f} kr")
    except ValueError:
        print("Felaktig inmatning. Ange ett decimaltal eller 'quit'.")

# Fråga om dricks
while True:
    user_input3 = input("\nAnge i ett heltal hur mycket dricks som ska läggas på (eller tryck Enter för 10%): ")
    if user_input3 == "":
        tip = 10
        break
    elif user_input3.isdigit() and int(user_input3) > 0:
        tip = int(user_input3)
        break
    else:
        print("Felaktig inmatning. Ange ett positivt heltal eller tryck Enter.")

# Räkna ut totalsumma med dricks
tip_cost = (tip / 100) * total_kostnad
total_med_dricks = total_kostnad + tip_cost
print(f"\n{tip}% dricks av {total_kostnad:.2f} kr är {tip_cost:.2f} kr.")
print(f"Den totala kostnaden med dricks är: {total_med_dricks:.2f} kr")

# Dela upp kostnaden per person
while True:
    user_input2 = input("\nHur många personer är ni? ")
    try:
        number_of_people = int(user_input2)
        if number_of_people <= 0:
            print("Antalet personer måste vara större än 0. Försök igen.")
        else:
            cost_per_person = total_med_dricks / number_of_people
            print(f"\nDet blir {cost_per_person:.2f} kr per person inklusive dricks.")
            break
    except ValueError:
        print("Felaktig inmatning. Ange ett heltal.")
