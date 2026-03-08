#du kan returnere en del av sen string med å bruke slice
#det skrivers på denne måte [3:5] så får du den delen av stringen slicet ut

x = "Hello, world!"
print (x[3:5])

#husk at første tegn i indexen alltid har posisjon [0]

#hvis du ikke skriver noe start på rangen så starter den bare på [0]
print (x[:7])

#samme for slutten, hvis du bare vil ha med hele "resten av stringen"

print (x[3:])

#du kan også bruke negativ indexing for å starte slicen fra andre siden av stringen
print (x[-5:-2])