"""F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
To specify a string as an f-string, simply put an f in front of the string literal,
 and add curly brackets {} as placeholders for variables and other operations."""

age = 30
txt = f"My name is Joel and I am {age}."
print(txt)

#A placeholder can contain variables, operations, functions, and modifiers to format the value.
price = 56
txt2 = f"The price of the item is {price} dollars."
print(txt2)

"""
A placeholder can include a modifier to format the value.
A modifier is included by adding a colon : followed by a legal formatting type, 
like .2f which means fixed point number with 2 decimals:
"""
txt3 = f"The price of the item is {price:.2f} dollars."
#in this example,:.2F gives 2 decimals
print(txt3)

#a placeholder can also contain math
txt4 = f"The price of the item is {50 + 7} dollars."
print(txt4)