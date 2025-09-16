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

3.Write a program that counts down from a given number to zero, but skips multiples of 3.
Instructions:

Ask the user for a starting number
Use a while loop to count down to 0
Skip numbers that are divisible by 3 (use the % operator)
Print "Blast off!" when you reach 0

Example Input/Output:
Enter starting number: 10
10
8
7
5
4
2
1
Blast off!

4. Create a simple shopping list program that lets users add items and display their list.
Instructions:

Start with an empty list
Ask the user how many items they want to add
Use a for loop to collect each item and add it to the list
Display the complete shopping list with numbers

Example Input/Output:
How many items do you want to add? 3
Enter item 1: apples
Enter item 2: bread
Enter item 3: milk

Your Shopping List:
1. apples
2. bread
3. milk

5.Write a function that analyzes a number and returns information about it.
Instructions:

Create a function called analyze_number(num) that takes one parameter
The function should return a string describing the number:

Whether it's positive, negative, or zero
Whether it's even or odd (only if it's not zero)


Call the function with different test numbers

Example Input/Output:
analyze_number(7) → "7 is positive and odd"
analyze_number(-4) → "-4 is negative and even"
analyze_number(0) → "0 is zero"
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

print("\nTesting Problem 1:")
    
name= input("what's your name? ")
age= int(input("what's your age? "))
color= input("what's your Favorite color? ")
print("Hi",name,"! According to your inputs, you are",age,"and your favorite color is",color)

print("\nTesting Problem 2:")
grade= input("What's your grade? ")
grade=int(grade)
if grade>=90:
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print("C")
elif grade>=60:
    print("Study!!")
elif grade>=50:
    print("Study!!")  
print("\nTesting Problem 3:")

chal= int(input("Pick a number "))
while chal>0:
    if chal % 3!=0:
        print(chal)
    chal=chal-1
print("Blast off!")

print("\nTesting Problem 4:")
items= int(input("How many stuff do you want on your grocery list? "))
groc=[]
for food in range(items):
    food= input("Add your items: ")
    groc.append(food)
print(groc)
print("\nTesting Problem 5:")

def analyze_number(num):
    if num%2== 1:
        print("This number is odd Mr.Frog  ")
    elif num%2 == 0:
        print(" This number is even stephen ")
    else:
        print("this number is a zero hero ")
    if num>=0:
        print("and this number is positive")
    else:
        print("and this number is negative")
num=input("Pick another number for me :) ")
num=int(num)
analyze_number(num)
