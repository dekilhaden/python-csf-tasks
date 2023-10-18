#Get a number from the user
number = int(input("Enter a number: "))
#Initialize a counter 
i = 1
#Display the multiplication table using a while loop
while i <= 20:
    result = number * i
    print(f"{number} x {i} = {result}")
    i += 1