#Get the name from the user
user_name = input("Enter your name: ")
#Convert the input to lowercase for case-insensitivity matching
user_name = user_name.lower()
#Initialize a variable to False
has_vowel = False 
#List of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}
#Initialize an index to 0
index = 0
while index < len(user_name) and not has_vowel:
    if user_name[index]in vowels :
       has_vowel = True
    index += 1
print(has_vowel)
