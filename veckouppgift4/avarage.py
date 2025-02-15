#Bygg en funktion med namnet average.
# Den ska ta parametrar: x och y. Båda ska vara tal.
# Funktionen ska returnera medelvärdet.
# Till exempel så räknar man ut medelvärdet av 4 och 8
# genom med formeln: (4 + 8) / 2, vilket blir 6.


def avarage(x,y):
    medel=0
    medel=(x + y) / 2
    return medel


medel_av_talen = avarage(2,8)
print(medel_av_talen)