while True:
    try:
        # Fråga användaren efter mål
        liverpool_goal = int(input("Hur många mål gjorde Liverpool? "))
        tottenham_goal = int(input("Hur många mål gjorde Tottenham? "))
        # Kontrollera att värdena inte är negativa
        if liverpool_goal < 0 or tottenham_goal < 0:
            print("Antalet mål kan inte vara negativt. Försök igen.")
            continue  # Gå tillbaka till början av loopen
        break  # Avbryt loopen om inmatningen lyckas
    except ValueError:
        print("Felaktig inmatning! Ange antal mål som ett heltal. Försök igen.")

# Jämför resultaten och skriv ut resultatet
if liverpool_goal > tottenham_goal:
    print(f"Liverpool vann! Liverpool gjorde {liverpool_goal} mål och Tottenham gjorde {tottenham_goal} mål.")
    more_goal = liverpool_goal - tottenham_goal
    print(f"Liverpool gjorde {more_goal} fler mål.")

elif liverpool_goal < tottenham_goal:
    print(f"Tottenham vann! Tottenham gjorde {tottenham_goal} mål och Liverpool gjorde {liverpool_goal} mål.")
    more_goal = tottenham_goal - liverpool_goal
    print(f"Tottenham gjorde {more_goal} fler mål.")

else:
    print(f"Det blev oavgjort! Liverpool gjorde {liverpool_goal} mål och Tottenham gjorde {tottenham_goal} mål.")
