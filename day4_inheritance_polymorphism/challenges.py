#Create a base class Animal with a method speak().
#Create two child classes: Dog and Cat that override speak() to return "Woof" and "Meow".
class Animal:
    def speak(self):
        return "general sound"
    
class Dog(Animal):
        def speak(self):
            return "woof"
        
class Cat(Animal):
        def speak(self):
            return "meow"
#Test
dog = Dog()
cat = Cat()

print("Dog says:", dog.speak())
print("Cat says:", cat.speak())

# Challenge 2: Using super() and Initializers
#Extend the previous challenge:
#Add an __init__ method in the Animal class that takes a name.
#Use super().__init__() in Dog and Cat to set the name.
#Add a method info() in each class that prints the name and what the animal says.

class Animal:
     def __init__(self, name):
        self.name = name

         def speak(self):
        return "Some sound"

    def info(self):
        return f"{self.name} makes a sound: {self.speak()}"
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Woof"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Meow"


# Test the classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.info())  # Buddy makes a sound: Woof
print(cat.info()) 