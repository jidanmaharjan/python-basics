#class
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print( f"Hello, {self.name}!")
    
# function
test =  MyClass("World")

test2 = MyClass("Python")

test.greet()  # This will return "Hello, World!"

test2.greet()  # This will return "Hello, Python!"

    
    