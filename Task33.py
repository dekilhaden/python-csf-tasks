# Get user input for grade as a string
grade_str = input("Enter your grade: ")

#Convert grade_str to an integer
grade = int(grade_str)

#Check the grade conditions and display the appropriate message
if grade >= 90:
    print("A")
elif 80 <= grade <= 89:
    print("B")
elif 70<= grade <= 79:
    print("C")
else:
    print("F")