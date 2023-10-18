user_inputs = []
for i in range(3):
    user_input = int(input(f"Please enter a number {i + 1}: "))
    user_inputs.append(user_input)

def is_even(numbers):
    even_numbers = []
    odd_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(even_numbers)
        else:
            odd_numbers.append(odd_numbers)
    print("even numbers: ", even_numbers)
    print("odd numbers:", odd_numbers)

is_even(user_inputs)