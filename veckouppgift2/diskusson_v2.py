#Vad är syftet med koden? Att räkna ut rabatt och pris beroende på hur mycket användaren handlar för
#Testkör koden med några olika värden.
#Finns det några direkta fel i koden? (fel som gör att programmet kraschar)
# Ja, final_price är en float, behöver konverteras till str för att kunna skrivas ut.
#Finns det logiska fel? (programmet gör något annat än det är tänkt)
#Ja, programmet kommer aldrig till andra if satsen, är det över 100 är första if satsen sann.
# ÄR priset under 100 blir det ingen rabatt alls, finns inget fall för det.
#is_member används inte heller och ingen riktig förklaring till hure den ska användas.
#Diskutera möjliga lösningar på felen ni hittat.
#Diskutera möjliga förbättringar på koden.

is_member = False
level1 = 100
level2 = 300
discount = 0
# kolla om användaren är medlem
user_input = input ("Är du medlem? ja/nej: ").strip().lower()
is_member = user_input == "ja"

#Om användaren är medlem får hen handla
if is_member:
    #felhantering, siffror accepteras bara
    try:
        price = input("Välkommen, köp något dyrt: ") #Be användaren mata in priset
        price = float(price)
    except ValueError:
             print("Ogiltigt pris, försök igen med ett numeriskt värde.")   
             exit()
    #Om användaren handlar under 100 kr blir det ingen rabatt
    if (price < level1):
        print(f"Du får tyvärr ingen rabatt eftersom din vara kostade under 100 kronor. Ditt pris blir: {int(price)} kronor")
    #Om användaren handlar över 100 kr blir det rabatt
    else:
        #Om användaren handlar 100-299 kr över 100 kr blir det 10% rabatt
        if (price >= level1 and price < level2):
            print(f"Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
            discount = discount + 10

        #Om användaren handlar över 299 kr 25% rabatt
        if (price >= level2):
           print(f"Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
           discount = discount + 25
        #Räkna ut det slutgiltliga priset
        final_price = price * (100 - discount) / 100
        print(f"Innan rabatten var priset {int(price)}")
        print(f"Efter rabatten blir priset: {int(final_price)} kronor")
else:
    print("Du måste vara medlem för att handla här.")

