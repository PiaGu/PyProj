#1g Funktionen "isinstance" kan kontrollera en variabels datatyp.
# Vad gör funktionen is_number? Går det att förbättra koden?
# DEn tar ett argument kollar ifall detta är en int, sedan om float.
# Är det ett tal returnetera den true annars false
# lägga in or för att korta koden.

def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False

print(is_number(5.5))
print(is_number(42))
print(is_number("text"))

#def is_number(x):
#    if isinstance(x, int) or is instance(x, float):
#        return True
#    else:
#        return False

#print(is_number(5.5))
#print(is_number(42))
#print(is_number("text"))