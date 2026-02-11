# Qn 1: Function Without Parameters.
# Area of a rectangle
width = int(input("Enter width: "))
length = int(input("Enter length: "))
area = width * length
print("The area of the rectangle is: ",area)


# Qn 2: Function With Parameters
def numbers(a,b):
    sum = a + b
    difference = a -b
    product = a * b
    division = a / b
    print("The sum of the numbers is:",sum)
    print("The difference of the numbers is: ",difference)
    print("The product of the two numbers is: ",product)
    print("The dividend of the two numbers is: ",division)

numbers(12,4)

#Qn 3: Control Statement (if...elif...else)
number = int(input("Enter your number: "))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")



#Qn 4: Loop with Arithmetic
def number_sum(x):
    sum = 0
    # for a in range(1,x+1):
    print("You entered the number is: ",x)
    print("The sum of numbers from",1,"to",x,"is: ",sum)

x = int(input("Enter your number here: "))

# Qn 5: While Loop
# number = int(input("Enter Your Number Here: "))

# while x <= number:
    # square

