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

def triangle():
  my_tri = {1: 'Length 1', 2: 'Lenght 2', 3: 'Lenght 3'}
  for key, value in enumerate(my_tri, 1):
    if key != 4:
      key = input(f"enter length of triangle for side {value} = ")
triangle()