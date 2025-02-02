# skriv in följande kod och modifiera den, så att den skriver ut figurerna a-j en i taget.

#Figur a
print("Detta är figur a")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 1:
            s += "#"
        else:
            s += "."
    print(s)

#Figur b
print("\nDetta är figur b")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)

#Figur c
print("\nDetta är figur c")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3 or x == 4 or x == 5:
            s += "#"
        else:
            s += "."
    print(s)

#figur c igen
print("\nDetta är figur c en gång till")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        s += "#" if x in (3, 4, 5) else "."
    print(s)



#Figur d
print("\nDetta är figur d")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if y == 3:  # Om det är den tredje raden,
            s += "#"
        elif x == 3:  # Annars, sätt # på tredje plats
            s += "#"
        else:
            s += "."
    print(s)


#Figur e
print("\nDetta är figur e")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if y == 1:
            s += "#" if x in (5, 6) else "."
        elif y == 2:
            s += "#" if x==5 else "."
        elif y == 3:
            s += "#" if x in (4, 5) else "."
        elif y == 4:
            s += "#" if x in (3, 5) else "."
        elif y == 5:
            s += "#" if x in (2, 5) else "."
        elif y == 6:
            s += "#" if x in (1, 5) else "."
        else:
            s += "."
    print(s)

#Figur F
print("\nDetta är figur f")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if y == 1:
            s += "#" if x in (1, 6) else "."
        elif y == 2:
            s += "#" if x in (2, 5) else "."
        elif y == 3:
            s += "#" if x in (3, 4) else "."
        elif y == 4:
            s += "#" if x in (3, 4) else "."
        elif y == 5:
            s += "#" if x in (2, 5) else "."
        elif y == 6:
            s += "#" if x in (1, 6) else "."
        else:
            s += "."
    print(s)

print("Detta är figur G")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x % 2 == 1:
            s += "#"
        else:
            s += "."
    print(s)

#Figur H
print("\nDetta är figur H")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if y == 1:
            s += "."
        elif y == 2:
            s += "#" if x in (2, 3, 4, 5, 6) else "."
        elif y == 3:
            s += "#" if x in (2, 6) else "."
        elif y == 4:
            s += "#" if x in (2, 6) else "."
        elif y == 5:
            s += "#" if x in (2, 3, 4, 5, 6) else "."
        elif y == 6:
            s += "."
        else:
            s += "."
    print(s)