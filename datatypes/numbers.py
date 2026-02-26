"""
Det er tre numeriske datatyper i Python
int
float
complex
"""

#variabler av den datatypen blir bestemt når du oppretter dem
x = 1 #int
y = 1.5 #float
z = 1j #complex

#for å verifisere datatypen bruker man type() funksjonen
print(type(x))

#int er integers, alle heltall uten komma (positivt eller negativt)
my_int = 1
my_int = 6335278283
my_int = -2343243
print (type(int))

#float er et flyttall, et tall med desimaler
my_float = 2.3
my_float = 2.3435435
my_float = -7.232
my_float = 1.2e40 #kan også være et scientific number (vet ikke helt hva det er)
print (type(float))

#complex numbers er skrevet med "j" som en ukjent del
my_complex = 3+5j
my_complex = 5j
my_complex = -5j
print (type(complex))

#du kan konvertere en variabels numeriske datatype fra en type til en annen
#untatt complex som ikke kan gjøres om til en annen data type
a = 5
aa = float(5)
print (aa)
print (type(aa))

"""
Python har ikke en random() funksjon for å genere et random tall
men du kan laste ned enn modul som heter random som lar deg gjøre det
"""
import random #Denne skal egentlig være i toppen av dokumentet
print (random.randrange(1, 10))