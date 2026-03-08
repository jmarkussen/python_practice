#denne delen handler om hvordan man modifiserer tekst strenger

#python has a set of built in methods to modify text strings

#the upper() method converts the string to UPPER CASE
x = "hello world"
print (x.upper())

#the lower() method does the exact same, but with lower case
y = "HELLO WORLD"
print (y.lower())

#the strip() method removes whitespace from the front or end of the string
#not from the middle 
z = "   Hello world   "
print (z.strip())

#the replace() method replaces a string with another string
#the first parameter is replaces from string with second parameter
print (x.replace("hello", "greetings"))

#the split() method returns a list where the text between the specified separator becomes the list items.
print (y.split(","))