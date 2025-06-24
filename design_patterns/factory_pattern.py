from abc import ABC, abstractmethod

# Step 1: Define the abstract Product
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    #make animal abstract base class

# Step 2: Create Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
#dog and cat implement animal
# Step 3: Create the Factory- decides whcih object to create
class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

# Step 4: Client Code - we use factory to get instances without calling dog or cat directly
if __name__ == "__main__":
    factory = AnimalFactory()

    animal1 = factory.create_animal("dog")
    print(animal1.speak())  # Output: Woof!

    animal2 = factory.create_animal("cat")
    print(animal2.speak())  # Output: Meow!
