user_name = input("Enter your name: ")
user_name = user_name.lower()
vowels = ['a', 'e', 'i', 'o','u']
count = 0
for char in user_name:
    if char in vowels:
        count+= 1
print("The number of vowels in your name is:", count)
