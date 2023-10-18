user_inputs = []
for i in range(3):
    user_input = int(input(f"Please enter a number {i + 1}: "))
    user_inputs.append(user_input)

def is_even(numbers):
    for number in numbers:
        if number % 2 != 0:
            return False
        return True
  
output = is_even(user_inputs)
print(output) 