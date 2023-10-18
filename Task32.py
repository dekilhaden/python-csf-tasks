#Get user input for age as a string
age_str = input("Enter your age: ")
 
 #convert age_str to an integer
age = int(age_str)

#Check the age conditions and display the appropriate message
if age > 22:
    print("I dont't care")
elif age == 18:
    print("You pass")
elif age < 17:
    print("You cannot touch beer")
else:
    print("You can drink")
