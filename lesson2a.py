# Python lists
# A list in python is a collection of items that are ordered in a certain way.
# A list is introduced by use of square brackets []
# The items of a list are stored inside of indexes. Note: In programming, we start counting from index Zeor(0)  
# A list is mutable i.e the contants of a list can be changed.

cars = ["BMW","Benz","Rolls Royce","Range Rover","Mc Laren","Hyndai","MayBach"]
print(cars)
print(type(cars))

# Accessing items of a list 
print(cars[2])
print("The car on index 4 is:", cars[4])

# List slicing- This is creating a list from a given bigger list.
print(cars[4:])
print(cars[:4])
print(cars[2:5])

# List Mutability
# We use the fuction append to add an item of a list .
cars.append("G-Wagon")
print(cars)

cars.append("Legacy")
print(cars)

# We use the pop function to remove an item at the end of the list
cars.pop()
print(cars)

# We can use an index to add items to a list
cars[5] = "Audi"
print(cars)

# We can use the sort function to sort out items in alphabetical order.
cars.sort()
print(cars)
cars.remove("Range Rover")
print(cars)
