# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

def check():
  # Set val to an empty string
  val = ""

  # While val doesn't equal end
  while val != "end":
    # Set val to input('say it')
    val = input('say it ')
    # Print input with length method
    print(f"What you entered is {len(val)} characters long")
    # However if val equals end
    if val == "end":
      # Stop loop
      break
#INVOKE FUNCTION HERE
check()