#Skriv en funktion som skriver ut det första talet i talserien som är större än 21.



    #Kolla om talet är större än 21
    # om det är större än 21 skriv ut
    #om inte addera första och andra talet
    #upprepa

def find_limit():
    total = 0  # Här sparar vi summan
    num = 1  # Starttal

    while total < 21:  # Loopa tills summan blir större än 21
        total += num  # Lägg till nästa tal
        num += 1  # Öka talet med 1

    print(f"Första talet som gör att summan går över 21 är: {num}")

    find_limit()