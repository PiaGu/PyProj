answer = 0
for i in range(1, 11):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))
# Svaret ska bli 55

#b Räkna ut summan av alla tal mellan 1 och 100. (inklusive 1 och 100, rätt svar ska bli 5050)

#svar = 0
#for i in range(1, 101):
#    svar += i
#    print(f"talet som adderas är nu {i}, summan är just nu: {svar}")
#print(f"Nu är loopen färdig! Den totala summan blir: {svar}")

i = 1
svar2 = 0
while i <= 100:
    print(f"Startvärde på i är: {i}")
    i += 1
    svar2 +=i
    print(f"talet som adderas är nu {i} och summan är just nu: {svar2}")
print(f"Slutsumman blir: {svar2}")