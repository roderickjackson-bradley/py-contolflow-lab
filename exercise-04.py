# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle



# This was such a pain build and an eye sour to look at
# Set a to an empty list
print("Please enter the three lengths of a triangle (one at a time)")

a = []

def triangle():
    
    prompt = int(input('a: '))
    push_to_list = a.append(prompt) 
    
    while a == []:push_to_list
    prompt1 = prompt
    
    if a != []:prompt = int(input('b: '))
    push_to_list 
    prompt2 = prompt
    
    if a != []:prompt = int(input('c: '))
    push_to_list
    prompt3 = prompt
    
    if a != []: 
        if prompt1 == prompt2 or prompt1 == prompt3 or prompt2 == prompt3 :
            tri_type = 'equalateral'
    
    if a != []:
        if prompt1 != prompt2 or prompt1 != prompt3 or prompt2 != prompt3 :
            tri_type = 'scalene'
            
    if a != []:
        if prompt1 != prompt2 or prompt1 == prompt2 or prompt1 == prompt3 :
            tri_type = 'isosceles'
    
    if a != []:
        if prompt1 == prompt2 or prompt1 == prompt2 or prompt1 != prompt3 :
            tri_type = 'isosceles'
            
    print(f"A triangle with sides of {prompt1}, {prompt2} & {prompt3} is a {tri_type}  triangle")
    
triangle()



# def triangle():
#   my_tri = {1: 'Length 1', 2: 'Lenght 2', 3: 'Lenght 3'}
#   for key, value in enumerate(my_tri, 1):
#     if key != 4:
#       key = input(f"enter length of triangle for side {value} = ")
# triangle()