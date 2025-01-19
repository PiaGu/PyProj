# Be om 3 heltal, splitta talen till 3 int variablar
# Kolla att inmatning är rätt, annars avsluta
try:
    tal1, tal2, tal3 = map(int, input("Ange tre heltal, separerade med mellanslag: ").split())
except ValueError:
    print("Felaktig inmatning. Se till att ange tre giltiga heltal! Programmet avslutas")
    exit()
    
#Summera ihop talen och skriv ut
total_sum= tal1 + tal2 + tal3
print(f"De tre talen är: {tal1}, {tal2}, {tal3}\nSumman av talen: {total_sum}")

#Jämför talen och ifall något tal är störst
if tal1 > tal2 and tal1 > tal3:
    print (f"Tal 1 är {tal1} vilket är större än tal 2 som är {tal2} och tal 3 som är {tal3}")
elif tal2 > tal1 and tal2 > tal3:
      print (f"Tal 2 är {tal2} vilket är större än tal 1 som är {tal1} och tal 3 som är {tal3}")
elif tal3 > tal1 and tal3 > tal2:
      print (f"Tal 3 är {tal3} vilket är större än tal 1 som är {tal1} och tal 2 som är {tal2}")

#Kolla ifall talen är lika stora
if tal1 == tal2 and tal1 == tal3:
    print(f"Alla talen är lika stora")
elif tal1 == tal2:
    print(f"Tal 1 är lika stort som tal2")
elif tal1 == tal3:
    print(f"Tal 1 är lika stort som tal3")
elif tal2 == tal3:
    print(f"Tal 2 är lika stort som tal3")
else:      #Om talen är olika, skriv ut det som är i mitten        
    if tal2 < tal1 < tal3:
        print(f"Tal 1 är i mitten")
    elif tal1 < tal2 < tal3:
        print(f"Tal 2 är i mitten")
    else:
        print(f"Tal 3 är i mitten")


