# 1. Create a list of numbers 1 to 10 and print only even numbers.
numbers = list(range(1, 11)) 
print(numbers)
for num in numbers:
    if num % 2 == 0:
        print(num)

# 2. Create a dictionary mapping numbers to their squares (1–5).
squares = {x: x**2 for x in range(1, 6)}
print(squares)



# 3. Add an item to a dictionary and remove one.
person ={
    "name": "Naz",
    "age": 23
}
person ["job"] = "doctor"
person.pop("age")

print(person)


# 4. Loop through a list of fruits and print each one.
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}:{fruit}")

# 5. Use list comprehension to create a list of squares (0–9).

    squares = [x**2 for x in range (10)]
    print(squares)

# 6. Use dict comprehension to create a dictionary of even numbers up to 10 and their cubes.
squares_dict = {x: x**3 for x in range (11) if x % 2 == 0}
print(squares_dict)


# 7. Use zip() to combine two lists: names and ages.
names = ["naz", "yas"]
ages =["23", "25"]
combined =list(zip(names, ages))
print(combined)


# 8. Use enumerate() to print each item in a list with its index.
city = ["london", "paris", "cairo"]
for index, cities in enumerate(city):
    print(f"{index}:{cities}")

# 9. Slice a list to get the last 3 items.
veg = ["carrot", "onion", "celery", "mushroom"]
print(veg[-3:])

# 10. Unpack a tuple into three variables and print them.
# 10. Unpack a tuple into three variables and print them.

person = ("Alice", 25, "Engineer")

name, age, profession = person

print("\n=== Challenge 10: Tuple Unpacking ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")
