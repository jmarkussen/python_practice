#Booleans represent one of two values: TRUE or FALSE

print(10 > 9)
print(2 == 5)
print(9 < 9)

#the results of these conditional statements will print either TRUE or FALSE in the terminal

a = 300
b = 56

if a > b:
    print("a is greater than b")
else:
    print(f"{b} is greater than {a}") #here is used some aditonal formatting also



#you are also allowed to evaluate variables with the bool() function
print(bool("Hello"))
print(bool(15))

"""
Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""

#Thats why all these examples will return TRUE
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#this however will return false
print(bool(0))
print(bool(""))

#not many values return false, but there are a few exceptions:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

"""
One more value, or object in this case, evaluates to False, 
and that is if you have an object that is made from a class with a __len__ function 
that returns 0 or False:
"""

class MyClass():
    def __len__(self):
        return 0

myobject = MyClass()
print(bool(myobject))

#you can create functions that return a boolean value
def my_function():
    return True
print(my_function())

#you can execute code based on the booleans answer to a statement

def my_function2():
    return False
if my_function2():
    print("YES!")
else:
    print("NO!")

"""Python also has many built-in functions that return a boolean value, like the isinstance() function, 
which can be used to determine if an object is of a certain data type:"""

x = 200
print(isinstance(x, int))