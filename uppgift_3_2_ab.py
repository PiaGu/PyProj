#2a Nu är det dags att köpa vinterkläder. Du ser en fin jacka som kostar 2000 kronor.
# Jackan är på rea, 50%. Skriv ett program som räknar ut hur mycket du behöver betala.
#2b Gör om programmet så att användaren kan skriva in en procentsats.
#Testa genom att hitta på en procentsats och räkna ut vad programmet ska svara med, innan du kör det.
# Till exempel 10%, som är 200 kr. Då ska jackan kosta 2000 - 200 == 1800 kr.

#Be användaren ange rabatt i procent utan procenttecken
rabatt_procent = input("Ange hur många procent rabatt det är med siffror utan procenttecken: ")
#Casta str till int
rabatt_procent = int(rabatt_procent)

#Be användaren ange nypriset på jackan i siffror
pris_jacka = input("Ange priset på jackan: ")
#Casta str till int
pris_jacka = int(pris_jacka)

#Räkna ut rabatten
rabatt_jacka = pris_jacka * rabatt_procent / 100

#Räkna ut nytt pris jacka
slutpris = pris_jacka - rabatt_jacka

#Skriv ut rabatt, jackans fullpris samt nytt pris med rabatt
print(f"Med {rabatt_procent}% rabatt på jackan som kostat {pris_jacka} kronor i fullpris blir det nya priset {slutpris} kronor")
