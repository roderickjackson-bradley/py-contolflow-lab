# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

def checks(string):
    
    # Make sure to make all string user input lowercase or the same case
    string = string.lower()
    # Store all vowels in this data set | for some reason I get errors if stored in a list or an array
    vowels = ('a','e','i','o','u')
    
    # Loop through the characters of the user's string input
    for char in string: 
        # If character that I looped through is a vowel
        if char in vowels: 
            print(f"The letter {string} is vowel")
        else:
            print(f"The letter {string} is consonant")
#INVOKE FUNCTION HERE
check('a')


