#variabler i python må ikke definere dataype
#kan ikke hete keywords eller tall osv.
x = 1
y = 2
z = 3

#Kan også definere variabler på en linje
a = b = c = "epler"

#printer ut alle tre variabler (funker også med ulike datatyper)
print (x, y, z)
#Operatører (x - osv.) legger sammen alle variabler (funker ikke med ulike datatyper)
print (x + y + z)

#Globale variabler, variabler utenfor en funksjon.
variabel = "supert"
def minfunksjon():
    print ("python er " + variabel)
minfunksjon()

#Samme men inni funksjon, så er den LOKAL
variabel = "supert"
def minfunksjon():
    variabel = "ekstra supert"
    print ("python er " + variabel)
minfunksjon()

#man kan også lage en global variabel inni en funksjon
def funksjon2():
   global myvar 
   myvar = 5
funksjon2()

#variabel er definert med nøkkelordet global inne i funksjon, men kan påkalles utenfor
print (myvar)

#Dette kan også endres inn i en funksjon
#Variabel definert utenfor funksjon
testfunc = 123
#local variabel gjort global inne i funksjon
def funksjon3():
   global testfunc 
   testfunc = 321
funksjon3()
#påkaller variabel utenfor funksjon, men tar den globale verdien
print(testfunc)

#Man kan også printe datatypen på en variabel med 'type()' funksjonen
dataVar = "9"
print(type(dataVar))