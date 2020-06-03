class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def say_hello(self):
        print("Hello, my name is "+ self.name + ".")


aerith = Person(1, "Aerith Gainsborough")
aerith.say_hello()