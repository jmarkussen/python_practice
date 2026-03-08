#strings er strenger med tekst i python
#man kan alltid printe strenger med den innebygde print() funksjonen


#i python så er "" og '' det samme.
print ("Hello, world!", 'Hello, world!')

#du kan ha qoute marks inne i strengen, så lenge det ikke er samme som i strengen.
print ("Kallenavnet hans var 'Pelle'")

#en variabel kan ha datatypen string
a = "hei"

#en string kan gå over flere linjer med samme teknikk som kommentarer
b = """
bla bla bla
ha ha ha
ja ja ja
""" #linjeskift i print() er på samme sted som i koden
print (b)

#strenger er også arrays
#det vil si at man kan finne position til et tegn i en string i python
test = "array"
print (test[1])
#her printes plass nummer [1] i arrayen so er ordet array, altså "r"

#siden strings er arrays så kan man også loope gjennom en string
for x in test:
    print (x)
#for mer informasjon om loops, se loops.py

#len() funksjonen viser lengden (antall tegn) i en string
my_var = "skolebrød"
print(len(my_var))

#nøkkelorden "in" sjekker om en string er en del av en annen string
my_var2 = "Norge vinner melodi grand prix i år!"
print ("melodi" in my_var2) #returnerer svaret som true/false

#dette er også mulig å gjøre i en "if statement"

my_var3 = "Norge vinner melodi grand prix i år!"
if "Norge" in my_var3:
    print ("Ja, Norge er i setningen")
else:
    print ("Nei Norge er ikke i setningen")

#du kan også gjøre det motsatt, med not in. 
my_var3 = "Norge vinner melodi grand prix i år!"
if "Norge" not in my_var3:
    print ("Nei, Norge er i setningen")
else:
    print ("Ja Norge er ikke i setningen")