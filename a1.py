# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
I'm learning Python basics in a high school programming class. I'm a Sophmore and I  have some experience with HTML from my ECS class last year but besides that, I only know the very basics of python like a for loop . Can you create 5-7 practice problems that cover:

Variables and basic data types

Conditionals (if/elif/else)

Loops (for and while)

Functions

Basic list operations

Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs.

"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
1.Write a program that asks the user for their name, age, and favorite color, then displays this information in a formatted message.
Instructions:

Use input() to get user information
Store each piece of information in a variable
Convert the age to an integer
Print a nice formatted message

Example Input/Output:
What's your name? Alex
How old are you? 15
What's your favorite color? blue

Hi Alex! You are 15 years old and your favorite color is blue.

2.Create a program that takes a numerical grade and converts it to a letter grade.
Instructions:

Ask the user for their numerical grade (0-100)
Use if/elif/else to determine the letter grade:

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F


Display both the numerical and letter grade

Example Input/Output:
Enter your grade: 87
Your grade of 87 is a B.

Enter your grade: 92
Your grade of 92 is an A.

"""











# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
    
name= input("what's your name? ")
age= int(input("what's your age? "))
color= input("what's your Favorite color? ")
print("Hi",name,"! According to your inputs, you are",age,"and your favorite color is",color)

print("\nTesting Problem 2:")
grade= input("What's your grade?")
if grade<89:
    print("A") 
print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


