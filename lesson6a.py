# Python module -> a file that contains python definitions, statements and/or functions.


def add():
    num1 = 20
    num2 = 30
    sum = num1 + num2
    print("The answer is: ",sum)

def subtract():
    x = 45
    y = 30
    difference = x-y
    print("The difference is: ",difference)


def rectagle_area():
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    area = length*width
    print("The area of the rectangle is: ",area)

# These functions defined on this particular file can be called into another file.
