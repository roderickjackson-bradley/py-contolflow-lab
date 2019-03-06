# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

# I really don't like this implementation but it's the
# only working solution I could come up with
def dog_age_val():
    age_val = int(input("Input a dog's age in human years: "))
    if age_val >= 2:
        reminder_cal = age_val - 2
        if reminder_cal == reminder_cal:
            dog_age = reminder_cal * 7
            if dog_age == dog_age:
                print(f" The dog's age in dog years is {dog_age + 20}!")                
#INVOKE FUNCTION HERE           
dog_age_val()