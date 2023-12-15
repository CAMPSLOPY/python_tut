def multiply_two_numbers(a,*b):
    print(a)
    for i in b:
        print(i)


print(multiply_two_numbers(4,90))


def add_two_numbers(num1,num2):
    return num1 + num2


print(add_two_numbers(1,90))

def area_of_circle(r, pi = 3.14,):
    area = pi * r ** 2
    return area

print(area_of_circle(34))

def find_odd_numbers(n):
    odd_num = []
    for i in range(n + 1):
        if i % 2:
            odd_num.append(i)
    return odd_num


print(find_odd_numbers(11))


print(area_of_circle(10))


def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total = total + num
    return total


print(sum_all_nums(1,2,4))

def convert_celsius_to_fahrenheit(C):
    return (C * 9/5) + 32

print(convert_celsius_to_fahrenheit(12))



def check_season(month):
    spring_months = ["March", "April", "May", "may"]
    summer_months = ["June", "July", "August"]
    autumn_months = ["September", "October", "November"]

    if month in spring_months:
        return "Spring"
    elif month in summer_months:
        return "Summer"
    elif month in autumn_months:
        return "Autumn"
    else:
        return "Winter"


# month_input = input(str("Enter the Month: ")).lower()


# result = check_season(month_input)

# print(result)


def calculate_slope(slope1,slope2,slope3,slope4):
    m = (slope2- slope1) / (slope4 - slope3)
    return m






x1, y1 = 1,2

x2, y2 = 3, 4

import cmath

print(calculate_slope(x1, y1, x2, y2))



def solve_quadratic_eqn(a,b,c):

    determinant = cmath.sqrt(b**2 - 4*a*c)

    x1 = (-b + determinant) / (2 * a)
    x2 = (-b - determinant) / (2 * a)

    solutions = (x1, x2)

    return solutions







a_coefficient = 1
b_coefficient = -3
c_constant = 2

print(solve_quadratic_eqn(a_coefficient,b_coefficient,c_constant))




def  print_list(*n):
    for i in n:
        print(i)

print_list(3,1,1,7,8)

def reverse_list(*arr):
    reversed_list = []
    for i in range(len(arr), 0, -1):
        reversed_list.append(i)
    return reversed_list





print(reverse_list(1,2,3,4,5,6))