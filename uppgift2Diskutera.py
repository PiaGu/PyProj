#Veckouppgift 1, övning 2, lösningsförslag
#Biljettpris, räknar ut pengar kvar, samt hälften av pengarna kvar.

biljettpris = 100  # biljettpris
pengarfickan = 200  # pengar på fickan
pengarkvar = pengarfickan-biljettpris # Pengar kvar
halvakvar= pengarkvar/2 #Hälften av summan som är kvar

print("Du har " +str(pengarfickan) + " kronor på fickan.")
print("Biljetten kostar " +str(biljettpris) + " kronor.")
print("Det blir " +str(pengarkvar) + " kronor kvar efter köpet.")
print("Hälften av de " +str(pengarkvar) +" kronorna blir "+str(halvakvar) + " kronor.")

