# Skapa listor
todo_list = []
done_list = []

while True:  # Huvudloopen som körs tills användaren väljer att avsluta
    print("\n** TODO LIST **")
    print("1. Se innehållet i din lista")
    print("2. Lägg till en ny uppgift")
    print("3. Markera en uppgift som klar")
    print("4. Se avklarade uppgifter")
    print("5. Avsluta programmet")

    choice = input("Välj ett alternativ (1-5): ")

    if choice == "1":  # Visa Att Göra Listan
        if not todo_list:
            print("\nDin att göra-lista är tom.")
        else:
            print("\nDin att göra-lista:")
            for item in todo_list:
                print(item)

    elif choice == "2":  # Lägg till en uppgift
        new_task = input("\nSkriv in en ny sak du måste göra: ")
        todo_list.append(new_task)
        print(f"Ok, lade till \"{new_task}\" i listan.")

    elif choice == "3":  # Markera en uppgift som klar
        if not todo_list:
            print("\nDet finns inga uppgifter att markera som klara.")
        else:
            print("\nVilken uppgift har du gjort klart?")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
            try:
                task_index = int(input("Ange siffran på uppgiften: ")) - 1
                if 0 <= task_index < len(todo_list):
                    done_list.append(todo_list.pop(task_index))  # Flytta till avklarade listan
                    print("Uppgiften har markerats som klar!")
                else:
                    print("Felaktigt val.")
            except ValueError:
                print("Du måste ange ett nummer.")

    elif choice == "4":  # Visa avklarade uppgifter
        if not done_list:
            print("\nDu har inga avklarade uppgifter.")
        else:
            print("\nDina avklarade uppgifter:")
            for task in done_list:
                print(f"- {task}")

    elif choice == "5":  # Avsluta programmet
        print("\nAvslutar programmet. Ha en bra dag!")
        break  # Stoppar loopen

    else:
        print("\nFelaktigt val, försök igen.")

