#1. Define and call a function that returns the square of a number.
def square(num):
   return num**2
print (square(5))
 

#2. Write a function that accepts any number of numbers using *args and returns their sum.
def sum_all(*args):
   return sum(args)

print(sum_all(1, 2, 3, 4))

#3. Write a function that accepts keyword arguments using **kwargs and prints them in key = value format.
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
       print(f"{key}= {value}")


print_kwargs(name="Alice", age=30, city="NY")


#5. Write a generator expression that generates even numbers up to 20.
#def evens ( x for x in range(21) if x % 2 == 0)
#for num in evens:
#print(num)


#6. Explain with code a use case for generators that demonstrate memory efficiency by iterating over a large range of numbers.
#def large_range():
 #  for num in range(1, 1_000_001):
  #    yield num

   #   gen = large_range()

#for _ in range(5):
 #   print(next(gen))





