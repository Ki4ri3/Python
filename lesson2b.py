# Tuple
# A tuple is an immutable type of a list; it cannot be changed
# To introduce a tuple, we use parentesis ()

counties = ("Nairobi","Mombasa","Kisumu","Nakuru","Kiambu","Murang'a")

print(counties)
print(type(counties))

# Tuple slicing
print(counties[3:])

#Accessing items of a tuple bu use of the indexes
print(counties[5])

# Note: Below will generate anerror
#Attribute error
counties.append("Machakos")
print(counties)