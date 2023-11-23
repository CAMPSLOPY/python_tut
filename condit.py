# Conditional execution: a block of one or more statements will be executed if a certain expression is true

# Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover if, else, elif statements. 
# The comparison and logical operators we learned in previous sections will be useful here.

# Task 1

# Enter_season = int(input("Enter your age:"))
# age_limit = 18
# # stat = 18

# if Enter_season >= age_limit:
#     print("You are old enough to learn to drive ")
# elif Enter_season < age_limit:
#     # we will subtract the user input from the age limit to get the remaining years needed before learning how to drive 
#     counter = age_limit - Enter_season
#     print(f"you need {counter} more years to learn to drive")


# # Task 2 AGE DIFFERENCE

# my_age = 31

# your_age = int(input("Enter your age: "))

# if my_age == your_age:
#     print("we are both ", my_age, " years old")
# elif your_age > my_age:
#     if your_age - my_age == 1:
#         print("you are 1 year older than me")
#     else:
#         counter = your_age - my_age
#         print(f"you are  {counter} years older than me")
# elif your_age < my_age:
#     counter = my_age - your_age
#     print(f"I am {counter} older than you ")

# TASK 3 

# A = int(input("Enter Number one: "))
# B = int(input("Enter Number two: "))

# if A > B:
#    print(A, "is greater than", B)
# elif A < B:
#    print(A, "is smaller", B)
# else:
#    print("Both are of the same value")



   # write a code that gives grade to students according to their scores 

# grade = int(input("Enter your Score:"))


# if grade > 80 and grade <=100:
#    print("Student Grade is A")
# elif grade > 70 and grade <= 79:
#    print("Student grade is B")
# elif grade > 60 and grade <= 69:
#    print("Student grade is C")
# elif grade >= 50 and grade <= 59:
#    print("Student grade is C")
# elif grade <= 49:
#    print("Student Grade is F")
# else:
#    print("Score not within the grade range")


# check SEASON of the year 

Enter_season = str(input("Enter Season: "))
season = Enter_season.lower()

if season in ["September","October", "November"]:
    print("Autumn")
elif season in ["December","January", "February"]:
    print("Winter")
elif season in ["March", "April", "May"]:
    print("Spring")
else:
    print("Summer")