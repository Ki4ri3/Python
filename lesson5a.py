# Python Functions
# They are block of code/statements that perform a given task/action. They can be reused throughout the program to perform different tasks.
#Functions are defined using the def keyword. (define)
# There are two main types of functions i.e:
#1. In-Built functions -> They come preinstalled with the intepreter i.e print(),pop(),range(),append()etc.....
#2. User defined functions -> They are created by a programmer to solve a given task.
#To deefine a function, you need to give it a name followed by parenthesis.
#For the functions, it is usually indented and to invoke a function we use the functions name.


def greetings():
    print("Hello, how are you?")

#below wwe call the function 
greetings()

print("==========================================")

# Addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is ", sum)

addition()

print("==========================================")
def multiplication():
    num1= 24
    num2= 3
    num3= 4
    multiplication =num1* num2* num3
    print("The multiple is: ", multiplication)

multiplication()

print("==========================================")

# below is a division function
def division():
    number1 = int(input("Enter the first number: "))
    number2= int(input("Enter the second number: "))
    quotient = number1/number2
    print("The answer is: ",quotient)

division()

for range in range(3):
    division()