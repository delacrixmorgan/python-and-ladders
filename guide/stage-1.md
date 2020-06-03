# 🍼

## Stage 1 - Python Basics 

Welcome to the World of Tomorrow! 

Well, it's my first time writing Python as well. Don't you worry! 

So, first things first!

___

### Hello World

```
println("Hello World")
println("Goodbye Cruel World")
```

Try to get this to print in your Terminal.


### 1 - If Statement

Tale as old as time, you'll need to assign variables to be true or false. So, it will display the messages respectively.

```
is_happy = True

if is_happy == True :
    print("Hello World")
else:
    print("Goodbye Cruel World")
```

### 2 - Data Types

There are Strings, Boolean and Integer.

**Strings**

```
first_name = "Aerith"
last_name = "Gainsborough"

print(firstName + " " + lastName)
```

Like you previously seen, this a String. You can do fancy stuff like manipulating them, adding them together.

For example, what I did here is just adding an empty white space between firstName and lastName.

**Boolean**
```
is_single = False

if is_single == True:
    print("I am single.")
else:
    print("I am in a relationship with Zack.")
```

True or false, simple as that. It can act like a flag too.

**Integer**

```
hp_points = 14

if hp_points < 25:
    print("I need healing.")
else:
    print("Nah, I'm good mate.")
```

Numbers, there are Int and Float.

Int are integers, Float are with decimal points.

```
gils = 500.14555555

print("I have %.2f gils" % round(gils,2))
print("I have %.2f gils" % round(gils))
```

This is how to round your float by setting your precision points.

### 3- Loops

```
crew = ["Vincent Valentine", "Tifa Lockhart", "Cloud Strife"]

i = 0

while i < len(crew):
    print(crew[i])
    i+=1
```

So, this a while loop. You have the variable `i` as a counter.
`i` is just a normal naming convention, it represents index.

### 4 - Class, Methods and Parameters (OOP Baby)

```
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def say_hello(self):
        print("Hello, my name is "+ self.name + ".")


aerith = Person(1, "Aerith Gainsborough")
aerith.say_hello()
```

Class is like a blueprint of your object, for instance id and name are its attributes.
When you create a new Person, you will have id and name.

Method is like a function, when you call it. It will run it.

For this example I've shown, then Person will have a method `say_hello()`. 
In which, I can define what is going to do.

For this case, it will say hello following with its name.

You'll notice something usual, it's call `self`. This is the syntax for python where it seems that you will need to pass in `self` as in the instances of the object itself inside.

So, that you can access to its attributes like how I've done.

### [👉🏻 Next Stage. Now, what?](/guide/stage-2-thought-process.md)