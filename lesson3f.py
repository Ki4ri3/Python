# Create a python program that is able to determine whether a number entered is an even number or odd number.
#number = int(input("Enter your number here:"))
#if number % 2 == 0:
 #   print("The number is even")
#else:
 #   print("The number is odd") 

# Create a python program that is able to determine whether a person can donate blood based on the age and weight of a person.. If the weight is greater than 50kg and age is above 18, then the person can donate ,else not possible.
weight = float(input("Enter your weight here: "))
age = int(input("Enter your age here: "))

if age >= 18 and weight >50:
    print("You can donate blood")
else: 
    print("you cannot donate blod")