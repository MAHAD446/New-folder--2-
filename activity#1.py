# Class creation
class myClass:

    # private variable
    __privateVar = 27

    # private method
    def __priMeth(self):
        print("I'm inside class myClass")

    # Function to print value of private variable
    def hello(self):
        print("Private Variable value: ", myClass.__privateVar)


# Object creation and method call
foo = myClass()
foo.hello()

# Attempting to call a private method (will raise an error)
foo.__priMeth  # This will cause an AttributeError