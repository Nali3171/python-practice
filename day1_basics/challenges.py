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