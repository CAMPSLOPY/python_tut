# # 30 days of programming 
import math


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

age = 3

height = 5.20





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
x_intercept = 1

slope_task8 = 2

# y intercept

# y = 2x - 2
# # set x = 0 and solve for y 
# y = 2(0) - 2
y_intercept= -2
print("x-intercept : ", x_intercept, " y-intercept : ", y_intercept, "and their slope is : ", slope_task8)

x1, y1 = 2,2
x2, y2 = 6, 10

slope_task9 = (y2-y1)  / (x2-x1)

euclidean_dist = ((x1 - y1 )**2 + (x2 - y2)**2) ** 0.5

print(slope_task9, euclidean_dist)

print(slope_task8 == slope_task9)

print('9.8' == 10)

code = 'python'
code2 = 'dragon'

print(len(code))
print(len(code2))
print(code == code2)

if 'on' in code and 'on' in code2:
    print("'on' is found both words")
else:
    print("'on' is not found in both words")

statement = 'I hope this course is not full of jargon'
if 'jargon' in statement:
   print('jargon is present in the statement')
else:
    print('jargon not present in the statement')

if 'on' in code and 'on' in code2:
    print('there is no  on in', {code}, ' and ', {code2})
else: 
    print('on is present in both', {code}, ' and ', {code2})


code_len = len(code)
code_len_float =float(code_len)
code_len_str = str(code_len_float)
print(code_len_str)
print(type(code_len_str))
print(type(code_len_float))

# how do i know if 4 is an even number

# GUESSING GAME 

# user_guess = int(input('Enter a number: '))

# if user_guess % 2 == 0:
#     print('The user entered an EVEN number')
# else:
#     print('user entered an ODD number')

if 7 // 3 == int(2.7):
    print(True)
else:
    print(False)

if '10' == 10:
    print(True)
else:
    print(False)

employee_hr = int(input('enter work Hours : '))
work_rate_per_hr = int(input('Enter rate per hour: '))
emp_earnings = employee_hr * work_rate_per_hr
print("your weekly earnings is : ", emp_earnings)