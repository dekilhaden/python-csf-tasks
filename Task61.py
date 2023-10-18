user_input = int(input("Please enter a number: "))
 
def is_even(number):
      if number % 2 == 0:
         return True
      else:
         return False
      
output = is_even(user_input)
print(output)