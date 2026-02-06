# Below is a grading system based on what a student will have attained.
marks =int(input("Enter student's marks: "))
# print("The entered marks is ", marks)
if marks > 0 and  marks < 30:
    print("Below average!")
elif marks >= 30 and marks < 40:
    print("Average")
elif marks >= 40 and marks < 70:
    print("Above Average")
elif marks >= 70 and marks <= 100:
    print("Excellent")
else:
    print("Invalid input!")