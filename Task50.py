num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
#Ensure num1 is smaller than num2
if num1 > num2:
    num1, num = num2, num1
#Initialize a variable to store the sum
total_sum = 0
#Calculate the sum of numbers between num1 and num2
while num1 <= num2:
    total_sum +=num2
    num1 += 1
#Display the final sum
print("The sum of numbers between" , "and", num2, "is", total_sum)