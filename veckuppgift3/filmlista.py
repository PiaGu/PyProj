#3 Träna på att skapa och manipulera listor. Alla uppgifter ska lösas med funktionerna som står i presentationen.
#3a Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar. Skriv ut hela listan 2med funktionen print.
#3b Lägg till "Fellowship of the ring" sist i listan.
#3c Lägg till "The two towers" på första platsen i listan. (index noll)
#3d Ta reda på vilken position (index) "Fellowship of the ring" har nu.
#3e Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
#3f Ta reda på hur lång listan är. (len)
#3g Vänd listan baklänges.
#3h Sortera listan stigande i bokstavsordning.

filmer: list[str] = ["Nalle Puh", "Kalle Anka", "Batman"]
print(f"Dessa filmer finns i listan: {filmer}")
filmer.append("Fellowship of the ring")
print(f"Denna läggs till: {filmer[-1]}")
print(f"Dessa filmer finns i listan nu: {filmer}")
filmer.insert(0,"The two Towers")
print(f"Dessa filmer finns i listan: {filmer}")
place_film = filmer.index("Fellowship of the ring")
print(f"Filmen Fellowship of the ring har plats {place_film}")
filmer.remove("Kalle Anka")
print(f"Dessa filmer finns i listan: {filmer}")
place_film = filmer.index("Fellowship of the ring")
print(f"Filmen Fellowship of the ring har plats {place_film}")
list_lenght = (len(filmer))
print(f"Listan filmer är {list_lenght} lång")
filmer.reverse()
print(f"listan har nu vänt på sig: {filmer}")
filmer.sort()
print(f"Filmerna är nu sorterade: {filmer}")
filmer.sort(reverse=True)
print(f"Filmerna är nu sorterade baklänges: {filmer}")