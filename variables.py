# # 30 days of programming 
import math
import os
import platform


# # day 2 excercise 

# first_name = 'tola'
# last_name = 'shobowale'
# full_name = 'tola shobowale'
# country = 'nigeria'
# city = 'brno'
# age = 31
# year = 2023
# is_married = False
# is_true = True
# is_light_on = True
# sex,sport,town,VG = 'male','football','lagos','xbox one s'

# print(len(first_name) == len(last_name))

# print(type(first_name))
# print(type(last_name))
# print(type(full_name))
# print(type(country))
# print(type(city))
# print(type(age))
# print(type(year))
# print(type(is_married))
# print(type(is_true))
# print(type(is_light_on))
# print(type(sex))
# print(type(sport))
# print(type(town))
# print(type(VG))


# num_one = 5
# num_two = 4
# total = num_one + num_two
# print(total)

# diff = num_one - num_two
# product = num_one * num_two
# print(product)

# division = num_one /num_two
# remainder = num_two % num_one 
# exp = pow(5, 4)
# floor_division = math.floor(division)

# print(floor_division)

# # area of a circle
# PI = 3.14
# r = 30

# area_of_circle = PI * r * r
# circum_of_circle = 2 * PI * r

# rad = float(input(" enter the radius of a circle: "))
# calc_area = PI * rad * rad

# print(calc_area)
# User_FirstName = input("Input your first Name: ")
# first_name = User_FirstName
# User_LastName = input(" Enter your Last Name: ")
# last_name = User_LastName
# User_country = input("Enter your country name: ")
# country = User_country
# User_age = input("Enter your age: ")
# age = User_age
# print(first_name, last_name,country,age)

# help("keywords")

# day 3 exercise 

# age = 3

# height = 5.20





# user_base = float(input("enter base number: "))
# user_height = float(input("enter base number: "))

# user_triang = math.floor( 0.5 * user_base * user_height)

# # print("the area of the triangle is : ",user_triang)

# cal perem of the triangle 
# side_a = int(input("enter side a : "))
# side_b = int(input("enter side b : "))
# side_c =int(input("enter side c : "))
# perem_triang = side_a + side_b + side_c
# print("The perimeter of the triangle is : ",perem_triang)
# user_length = int(input("enter the area length : "))
# user_width = int(input("enter the area width : "))
# user_area_rec = user_length + user_width
# user_perem_rec = 2 *( user_length + user_width)
# print(" The area of the user rectangle is : ", user_area_rec , " and the perimter of the rectangle is : ", user_perem_rec)

# pi = 3.14 
# r = int(input("enter the radius of a circle : "))
# cirle_area = pi * r * r 
# circum_area = 2 * pi * r
# print(" The area of the user circle is : ", cirle_area , " and the circumference of the circle is : ", circum_area)

#  intercept formular 

# y = mx + c 

# to find the y intercept we will sub the (x) for (0)

# x-intercept 
#  x = 2x - 2
# # set y = 0 and solve for x
# 0 = 2x - 2
# 2x = 2
# x = 2/2
# x_intercept = 1

# slope_task8 = 2

# y intercept

# y = 2x - 2
# # set x = 0 and solve for y 
# y = 2(0) - 2
# y_intercept= -2
# print("x-intercept : ", x_intercept, " y-intercept : ", y_intercept, "and their slope is : ", slope_task8)

# x1, y1 = 2,2
# x2, y2 = 6, 10

# slope_task9 = (y2-y1)  / (x2-x1)

# euclidean_dist = ((x1 - y1 )**2 + (x2 - y2)**2) ** 0.5

# print(slope_task9, euclidean_dist)

# print(slope_task8 == slope_task9)

# print('9.8' == 10)

# code = 'python'
# code2 = 'dragon'

# print(len(code))
# print(len(code2))
# print(code == code2)

# if 'on' in code and 'on' in code2:
#     print("'on' is found both words")
# else:
#     print("'on' is not found in both words")

# statement = 'I hope this course is not full of jargon'
# if 'jargon' in statement:
#    print('jargon is present in the statement')
# else:
#     print('jargon not present in the statement')

# if 'on' in code and 'on' in code2:
#     print('there is no  on in', {code}, ' and ', {code2})
# else: 
#     print('on is present in both', {code}, ' and ', {code2})


# code_len = len(code)
# code_len_float =float(code_len)
# code_len_str = str(code_len_float)
# print(code_len_str)
# print(type(code_len_str))
# print(type(code_len_float))

# how do i know if 4 is an even number

# GUESSING GAME 

# user_guess = int(input('Enter a number: '))

# if user_guess % 2 == 0:
#     print('The user entered an EVEN number')
# else:
#     print('user entered an ODD number')

# if 7 // 3 == int(2.7):
#     print(True)
# else:
#     print(False)

# if '10' == 10:
#     print(True)
# else:
#     print(False)

# employee_hr = int(input('enter work Hours : '))
# work_rate_per_hr = int(input('Enter rate per hour: '))
# emp_earnings = employee_hr * work_rate_per_hr
# print("your weekly earnings is : ", emp_earnings)


# user_year = int(input('Enter number of years you have lived :'))
# sec_per_yr_lived = 31536000
# calc_year_per_sec = user_year * sec_per_yr_lived

# print('You have livedd for ',calc_year_per_sec, ' seconds')



# define num of rows

# num_rows = 5
# for n in range(1, num_rows + 1):
#     row_2 = 1
#     row_2 = n ** 3
#     row_4 = n ** 4
#     row_5 = n ** 5
#     row_6 = n ** 5
 
#     print(f"{n} 1 {row_2} {row_3} {row_4} {row_5}")


# Define the number of rows for the table
num_rows = 5

# Print the table header


# # Iterate through each row
# for n in range(1, num_rows + 1):
#     # Initialize variables to store the calculated values
#     n_power_1 = 1
#     n_power_2 = n
#     n_power_3 = n ** 2
#     n_power_4 = n ** 3

    
#     # Print the row values
#     print(f"{n} {n_power_1} {n_power_2} {n_power_3} {n_power_4}")


# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
# # formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
# formated_string = 'The following are python libraries:%s' % (python_libraries)
# print(formated_string)

# word = "my name is joshua \n what is your name?"
# print('Days\tTopics\tExercises')
# print(word)

# language = 'python'
# first_letter = language[0]
# print(first_letter)
# last_letter = language[-1]
# last_letter_2 = len(language) - 1
# print(last_letter)
# print(last_letter_2)

# print("hello world!")



# def shutdown():
#     if platform.system() == "Windows":
#         os.system('shutdown -s')
#     elif platform.system() == "Linux" or platform.system() == "Darwin":
#         os.system("shutdown -h now")
#     else:
#         print("Os not supported!")

# def restart():
#     if platform.system() == "windows":
#         os.system("shutdown -t 0 -r -f ")
#     elif platform.system() == "Linux" or platform.system() == "Darwin":
#         os.system("reboot now")
#     else:
#         print("Os not supported!")
# command = input("use \'r\' for restart and \'s\' for shutdown: ").lower()

# if command == "r":
#     restart()
# if command == "s":
#     shutdown()
# else:
#     print("wrong letter")

# challenge = " thirty days of python"
# print(challenge.count('o'))
# print(challenge.rfind('th'))

# CHALLENGE EXERCISE DAY 4
statement = ['Thirty', 'Days', 'Of', 'Python']
statement_2 = ['Coding', 'For' , 'All']
concat_statement = ' '.join(statement)
concat_statement_2 = ' '.join(statement_2)
print(concat_statement_2)

company = concat_statement_2
company_len = len(company)
block_case = company.upper()
small_case = company.lower()
capitalize_comp = company.capitalize()
title_comp = company.title()
swap_comp = company.swapcase()
slice_comp = company[0:6]
state = "Coding"

if(company.__contains__(state)):
    print(f"{state} is avalable in the statement")
else:
    print(f"{state} not available in the statement")

company_3 = company.replace("Coding", "Python")
company_4 = company_3.replace("All", "Everyone")
tech = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
tech_split = tech.split(",")

split_statement = company.split(" ")
com_index =company[0]
com_last_index =company[-1]
com_tenth_index =company[10] #the index at the 10th value is space
# lets create an acronym from the "python for all"

# step 1 
#  split the statement into individual elements

# step 2 Iterate through each words to get the position of the first letter in each words index

acronym = []
words = company_3.split()

for word in words:
    acronym +=word[0]

print(acronym)