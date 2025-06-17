#1. Define a simple class Car with an attribute brand. Create an instance and print the brand.
class Car:
    brand = None

car1 = Car()
car1.brand = "Toyota"

print(car1.brand) 
#2. Add an __init__ constructor to Car to initialize brand and year attributes.

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

car1 = Car("Toyota", 2020)
print(car1.brand)  # Output: Toyota
print(car1.year)   # Output: 2020



#3. Create two instance variables and one class variable in a class Dog. Demonstrate the difference by creating two dogs.
class Dog:
    species = "canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("nazzy", 4)
dog2 = Dog("bob", 7)

print(dog1.name, dog1.species)  
print(dog2.name, dog2.species)  

Dog.species = "Feline"

print(dog1.species)
print(dog2.species)


#4. Add a __str__ method to Car that returns a user-friendly string like "Car(brand=Toyota, year=2020)". Print the car instance.
class Car:
     def __init__(self, brand, year):
        self.brand = brand
        self.year = year

        def __str__(self):
            return f"Car(brand={self.brand}, year={self.year})"

car1 = Car("Toyota", 2020)
print(car1)



#5. Add a __repr__ method to Car that returns a string that looks like the code to create the object, e.g. "Car('Toyota', 2020)".
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def __repr__(self):
        return f"Car('{self.brand}', {self.year})"
    car1 = Car("Toyota", 2020)
print(repr(car1))



