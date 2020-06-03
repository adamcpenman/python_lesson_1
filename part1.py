# print hello world
print("Hello, world!")

# declare a variable
name = "Adam"
print(name)

# string concatenation
print('Hello ' + name)
# `Hello ${name}`
print(f'Hello {name}')

# Data structures

# Array = Lists
p = [10, 20, 30, 60, "Orange"]
print(p)
# add an element to the end of P
p.append(77)
print(p)

# Lets loop over the list of P and print every element
for element in p:
    print(element)
print('we printed it again')


# lets print the index and element at the index of P
for (index, element) in enumerate(p):
    print(f'Element at {index} is {p[index]}')

# another way to create a list
numbers = [1, 4, 9, 16, 25]
# create a new list of squares from the numbers list
squares = []
for num in numbers:
    squares.append(num*num)
print(squares)

# lets use List Comprehensions
cooler_square = [num*num for num in numbers]
print(cooler_square)

# Lets create a list of just even numbers
evens = [num for num in numbers if num % 2 == 0]
print(evens)

names = ["Adam", "Ally", "Sam", "Frank", "Sally"]


s_names = [name.capitalize() for name in names if name[0].lower() == 's']
print(s_names)

s_names_verbose = []
for name in names:
    if(name[0].lower() == 's'):
        s_names_verbose.append(name.capitalize())

print(s_names)

# Dictionaries!
# Otherwise know as maps/hashmaps/objects
# A key -> value data structure
new_dict = {}

# create a dictionary with some keys and values
food_dict = {
    'apple': 'is a fruit',
    'carrot': 'is a veggie'
}
print(food_dict)

# add a new key value pair
food_dict['cucumber'] = 'is maybe a veggie'
print(food_dict)

# access and print a specific element in food_dict
chosen_food = 'apple'
print(food_dict[chosen_food])

# iterate through keys and values of a dictionary
# for element in dict, do some code
for key, value in food_dict.items():
    print(f'{key} : {value}')

# how can we ckeck if element exisits in a dictionary?
# is apple in food_dict?
print('apple' in food_dict)
print('banana' in food_dict)

#tuples and sets

# Tuples
tup = (1, 2, 3, 4)
for item in tup:
    print(item)


# access a particular element
print(tup[1])

# Sets are basically dictionaries without values
fruit = {'cucumber', 'apple', 'banana'}

for item in fruit:
    print(item)

if 'cucumber' in fruit:
    print('I dont think its a fruit')
