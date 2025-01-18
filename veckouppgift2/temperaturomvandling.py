#Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.
#Version 1, exempel på output:
#Skriv in en temperatur i grader Celsius: 22
#Det blir 71.6 grader Fahrenheit.
#Version 2: fråga först användaren om man vill ange temperaturen i Celsius eller Fahrenheit.
# Sedan räknar programmet om till den andra temperaturen.
#Version 3: om temperaturen som omvandlas är under 10°C ska programmet dessutom säga till användaren
# att ta på sig vinterkläder. Och om temperaturen är minst 20°C ska det föreslå att man packar badkläder.
#Formel för konvertering mellan temperaturenheter:
#C = (F - 32) / 1.8
#F = 1.8 * C + 32

try:
    temperaturval = input ("Ange F om du vill mata in temperatur i Fahrenheit eller ange C ifall du vill mata in temp i Celcius: ").strip().upper()
    print(f"du har valt {temperaturval}")
    if temperaturval == "C":
        try:
            temperatur_celcius = int (input("Ange antal grader i Celcius: "))
        except ValueError:
            print("Ogiltig inmatning för Celsius. Ange ett heltal!")
            exit()
        fahrenheit = 1.8 * temperatur_celcius + 32
        print(f"Temperaturen {temperatur_celcius} grader celcius motsvarar {fahrenheit:.1f} grader fahrenheit." )
        if temperatur_celcius >= 20:
            print(f"Packa badkläder, eftersom temperaturen är {temperatur_celcius} grader celcius")
        elif temperatur_celcius < 10:
            print(f"Ta på dig vinterkläder, eftersom temperaturen är {temperatur_celcius} grader celcius")

    elif temperaturval == "F":
        try:
            temperatur_fahrenheit = int (input("Ange antal grader i Fahrenheit: "))
        except ValueError:
            print("Ogiltig inmatning för Fahrenheit. Ange ett heltal!")
            exit()
        celcius = (temperatur_fahrenheit - 32) / 1.8
        print(f"Temperaturen {temperatur_fahrenheit} grader fahrenheit motsvarar {celcius:.1f} grader celcius")
        if temperatur_fahrenheit >= 68:
            print(f"Packa badkläder eftersom temperaturen är {temperatur_fahrenheit} grader fahrenheit")
        elif temperatur_fahrenheit < 50:
            print(f"Ta på dig vinterkläder, eftersom temperaturen är {temperatur_fahrenheit} grader fahrenheit")
    else:
        print("Du valde inget giltligt alternativ")

except ValueError:
    print(f"Felaktig inmatning, ange en giltlig temperatur i heltal")

