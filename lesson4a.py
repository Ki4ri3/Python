# Nested If statements
# Is a statement that is within another if statement.

age = 21
weight = 46

if age > 15:
    if weight > 50:
        print("You can donate blood.")
    else:
        print("You cannot donate blood because of your weight")
else:
    print("You cannot donate blood because of your age.")