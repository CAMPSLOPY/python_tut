# Conditional execution: a block of one or more statements will be executed if a certain expression is true

# Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover if, else, elif statements. 
# The comparison and logical operators we learned in previous sections will be useful here.

# Task 1

user_input = int(input("Enter your age:"))
age_limit = 18
# stat = 18

if user_input >= age_limit:
    print("You are old enough to learn to drive ")
elif user_input < age_limit:
    # we will subtract the user input from the age limit to get the remaining years needed before learning how to drive 
    counter = age_limit - user_input
    print(f"you need {counter} more years to learn to drive")
