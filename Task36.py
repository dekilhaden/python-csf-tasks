#Define a variable called "score" and get its valure frommmmm user input
score = input("Enter your score: ")
#Convert the input to an integer
score = int(score)
#Check the score
if score >= 90:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
elif score < 60:
    print("F")
else:
    print("Invalid score")