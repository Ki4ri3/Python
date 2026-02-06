# Dictionary - a data type that stores data in terms of key-value pair.
# It is introduced by the use of curly braces {
# The values stored inside of a dictionary can be of any data type.
# To access the values in a dictionary we use the keys


phonebook = {
    "Kiarie" : "+254756329764",
    "Mary": "+2541342435879",
    "Stephen" : "+254756323487"
}

# Showing the entire dictionary
print(phonebook)
print(type(phonebook))

# Printing out Kiarie's number
print(phonebook["Kiarie"])

print('=======================================')

player = {
    "Name" : "Messi",
    "Age" : 40,
    "Teams" : ["PSG","Barcelona","Argentina"]
}
print(player["Teams"][1])