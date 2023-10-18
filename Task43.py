user_name = input("Enter your name: ")
user_name = user_name.lower()
vowels = ['a', 'e', 'i', 'o', 'u']
has_vowel = any(char in vowels for char in user_name)
print(has_vowel)
