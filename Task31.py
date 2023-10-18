#Get user input for age as a string
age_str = input("Enter your age: ")
 
 #convert age_str to an integer
age = int(age_str)

#Check if age is above 18 and display the appropriate message
if age > 18:
    print("you can drink")
else:
    print("Plese grow older")