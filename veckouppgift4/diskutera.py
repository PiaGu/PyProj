# En funktion som heter foo, tar ett argument och skriver ut test.
# Använder inte argumentet här alls, skriver ut test oavsett vad som skickas in.
#1a
#def foo(t):
#    print("test")

#foo("hej")

# Här lagt in att argumetnet ska skrivas ut.
def foo(t):
    print(f"{t} test")
foo(t="hej")

#1b
# Funktionen defineras, tar 2 argument, mutltiplicerar agrumenten och returnerar svaret.
# Man här anropas inte funktionen utan det kommer bara skrivas ut 3,5
#def fun1(x, y):
#    return x * y
#print(3, 5)

#def fun1(x, y):
#   return x * y
#
#fun1(3, 5)



#1c DEfinierar funktion fun1, 2 argument, returnerar produkten av de 2 argumenten.
#Skriver ut resultatet
def fun1(x, y):
    return x * y

print(fun1(3, 5))

#1d
#Definierar funktion fun2, 1 argument, 5*i returnerar svaret.
#Anropar funtionen 2 gånger med olika argument, adderar argumenten och anropar en gång till
#Skriver ut resultatet
def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y)) #fun2 (5*2 + 5*3) = fun (25) = 125
print(a)


#1e a är 5,adderar 2 tilla blir 7, funktionen fun3 tar 1 argumwnt lägger till 1 .
#men anropas inte hät. 2 aderas till a skriver ut 7
a = 5
def fun3(a):
    a += 1

a += 2
print(a)

#1f anropar foo2 men skickar inte med ett argument, Försöker sedan anropa goo med foo2 som ett av argumenten.
#Fattar inte denna
def foo2(i):
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo2, 3);
print(a)



