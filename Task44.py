user_name = input("Enter your name: ")
user_name = user_name.lower()
vowels = ['a', 'e', 'i', 'o','u']
count = 0
index = 0
while index<len(user_name):
    if user_name[index] in vowels:
        count += 1                    # Increment count if a vowel is found
    index += 1
print("The number of vowels in your nmae is:", count)
