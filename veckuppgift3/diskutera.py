#Skriver ut 0-4, sedan en tom rad, sedan 6-9
#for i in range (10):
#    if i == 5:
#        print("")
#    else:
#        print(i)
#    i = i + 1
# samma som: i += 1
#from veckuppgift3.diskutera5 import message      # inte en aning var denna raden kom ifrån

#counter = 0
#for i in range(6):
#    print(f"i innan addition: {i}")
#    counter += i
#print(f"Summan av alla tal i range blir: {counter}")

#x = 0
#y = 1
#print(f"x är : {x}, y är {y}")
#Så länge y är mindre än 10
#while y < 10:
    #Om divitionen inte har någon rest är det ett jämt tal.
    #Alltså, alla jämna tal, minska x med y
#    if y % 2 == 0:
#        print(f"y är {y}, alltså jämt tal")
#        x -= y
#        print(f"Här minskas x med y. y är här: {y}, x blir: {x}")
     #Om inte talet är jämt, alltså ojämnt
#    else:
    #multplicera y med y och addera till x
#        x += y * y
#        print(f"y som är {y} multipliceras med y och adderas till x som blir: {x}")
    #Addera 1 till y
#    y += 1
#    print(f"y adderas med 1 och blir {y}, ")

#message = "its_time_to_get_coding"
#print(message[3:7])
#print(message[4:8])

for y in range(1, 7):
    s = ""
    for x in range(1, 9):
     #   if x == y:
        if x == y+2:
            s += "#"
        else:
            s += "."
    print(s)


