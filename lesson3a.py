# Boolean - This is a data type that evaluates either True or False.

isRaining = False
print(isRaining)
print(type(isRaining))


paidloan = True
print(paidloan)
print(type(paidloan))

# Comparison operators: Used to compare two or more statements. They usually return a boolean answer.

number1 = 2
number2 = 5
print("Is number1 greater than number two?", number1 > number2)
print("Is number1 less than number two?", number1 < number2)
print("Is number1 greater than or equal to  number two?", number1 >= number2)
print("Is number1 less than or equal to number two?", number1 <= number2)
print("Is number1 equal to number two?", number1 == number2)
print("Is number1 not equal to number two?", number1 != number2)

# Logical Operators
# Logical AND
# It returns true if and only if the condition/statement evaluates to true
print((3 > 1) and (7 > 6))

# Logical or
# It evaluates to true if one of the statements/conditions is true.
print((3 > 1) or (7 < 6))

# Logical not
# it is used to negate a statement/condition.
print(not(90 > 70))
