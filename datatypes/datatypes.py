"""
I programmering er datatyper et viktig konsept
variabler kan inneholde ulike datatyper, og ulike datatyper gjør forskjellige ting
Python har følgende datayper innebygd:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
#Man kan  printe datatypen på en variabel med 'type()' funksjonen
x = "9"
print(type(x))

#i python så settes datatypen når du definerer variabelen
y = 5 #denne er automatisk en int(heltall)

#du kan også velge å definere selv om du ønsker det
z = float(5.5)


#Det er tre numeriske datatyper i python
#int, float og complex
x = 1
y = 1.1
z = 1j

print(x, y, z)

