num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    num1, num2 = num2, num1
total_sum = 0
for number in range(num1, num2 +1):
    total_sum += number
print("The sum of numbers between", num1, "and", num2, "is", total_sum)
