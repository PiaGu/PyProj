#Uppgift 3 Använda variabler och datatyper
#1a Använd input för att be användaren om ett heltal.
# Spara värdet i en variabel. Omvandla variabelns värde till ett heltal,
# och skriv ut det för att testa om du har gjort rätt.

#Be användaren om ett heltal
user_input_str = input("Ange ett tal mellan 1-100: ")
#print("Variabeln user_input_str är av datatypen: ", type(user_input_str))
#print ("och har värdet: ",user_input_str)

#Med F string istället
print(f"Variabeln user_input_str är av datatypen: {type(user_input_str)}")
print(f"och har värdet: {user_input_str}")



#Konvertera från sträng till heltal
user_input_int= int(user_input_str)
#print("Variabeln user_input_int är nu av datatypen: ", type(user_input_int))
#print ("och har värdet: ",user_input_int)

#Med f string istället
print(f"Variabeln user_input_int är av datatypen: {type(user_input_int)}")
print(f"och har värdet: {user_input_int}")