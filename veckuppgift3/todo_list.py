

new_task = 'uppgift'
to_do_list: list[str] = []
done_list: list[str] = []
user_choice = 0
remove_task = 'bort'



# Meny
print("Vad vill du göra? Välj ett alternativ.")
print(" välj 1: Skriv ut Att göra lista")
print(" välj 2: Lägg till uppgift i Att göra listan")
print(" välj 3: Markera uppgift som klar och flytta till done list")
print(" välj 4: Flytta uppgift från done list till att göra listan.")
print(" välj 4: Avsluta program" )

user_input = input("Ditt val: ")

if user_input.isdigit():
  user_choice = int(user_input)
  if user_choice == 1:
    for x in to_do_list:
      print(x)
  elif user_choice == 2:
    user_input1 = input("Lägg till en uppgift i listan: ")
    to_do_list.append(user_input1)


    for x in to_do_list:
      print(x)

  elif user_choice == 3:
    print("\nFelaktig inmatning! Ange ett heltal mellan 1 och 3")

  elif user_choice == 3:
    print("\nFelaktig inmatning! Ange ett heltal mellan 1 och 3")
else:
  print("\nFelaktig inmatning! Ange ett heltal mellan 1 och 3")



#user_input = input("Lägg till en uppgift i listan: ")


#to_do_list.append(user_input)

#