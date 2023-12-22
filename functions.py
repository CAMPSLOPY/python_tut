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

def capitalize_list_items(*n):
    capital = []
    for i in range(len(n)):
        cap = n[i].upper()
        capital.append(cap)
    return capital
# print(capitalize_list_items("tola", "joshua", "fe fundinfo"))





list_items = ["tola", "joshua"]

# for i in range(len(list_items)):
#     list_items.insert(0,2)
#     print(list_items)
#     break


def add_item(original_list, new_item):

    new_list = original_list.copy()

    new_list.append(new_item)

    return new_list


print(add_item(list_items, "muyi"))




numbers = [2, 7, 9]




print(sum)

def remove_item(original_list, new_item):
    
    # check if new item already exist in the original list

    if new_item in original_list:
        original_list.remove(new_item)
    else:
        print(f"{new_item} not found in the list")
    
    return original_list
    

print(remove_item(numbers, 9))






# for num in range(len(numbers)):
#     print(num)
#     if num == 3:
#         numbers.remove(num)
#         print(numbers)







def sum_of_numbers(num):
    sum = 0
    for n in range(num):
        sum +=  n + 1
    return sum



# print(sum_of_numbers(5))






# oddd = [1,2,3,4,5,6]
# odd_adder = 0
# eve_list =[]
# for odd in oddd:
#     if odd % 2:
#         print(odd)
#         odd_adder += odd
# print(odd_adder)

def sum_of_even(even_number):
    even_sum = 0
    even_number_list = []
    for eve in range(even_number):
        # attach the even number to a list
        even_number_list.append(eve)
    for even in even_number_list:
        if even % 2 == 0:
            even_sum += even
    return even_sum
        



def sum_of_odd(odd_number):
    odd_sum = 0
    odd_number_list = []
    for odd in range(odd_number):
        # attach the odd number to a list
        odd_number_list.append(odd)
    for od in odd_number_list:
        if od % 2:
            odd_sum += od
    return odd_sum


print(sum_of_even(100))
print(sum_of_odd(100))
print(sum_of_odd(100))