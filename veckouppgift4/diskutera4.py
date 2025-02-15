#1i En uppgift i tre delar:
#Lista ut vad som är funktionens syfte, baserad på namn och sammanhang.
#Lista ut vad som ska vara det förväntade resultatet för de tre testlistorna.
#Rätta felen, så funktionen gör det den ska.
from tarfile import version

# Funktionen ska hitta minsta numret i en lista och skriva ut svaret
#Här skrivs det ut i funktionen. DEt returnerade värdet används inte alls.
#Logiken fungerar inte i funktonen. Borde loopa genon listan och jämföra nummer för nummer

#def find_min(numbers):
#    counter = 0
#    for item in numbers:
#        if item < counter:
#            counter = item
#    print(f"The smallest item is: {counter}")
#    return counter

#find_min([-110, 3, -4, -11])
#find_min([])
#find_min([100])
# ÄR 100 mindre än 0? Nej returnera 0
 # Rättad version
def find_min(numbers):
    if not numbers:  # Hantera tom lista
        print("The list is empty, no minimum value.")
        return None

    counter = numbers[0]  # Starta med första talet i listan
    for item in numbers:
        if item < counter:
            counter = item  # Uppdatera om vi hittar ett mindre värde

    print(f"The smallest item is: {counter}")
    return counter


# Testfall
find_min([10, 3, -4, -11])  # Output: -11
find_min([])  # Output: "The list is empty, no minimum value."
find_min([100])  # Output: 100
