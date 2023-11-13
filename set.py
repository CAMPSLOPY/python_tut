# Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. 
# The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements.
#  In Python set is used to store unique items, and it is
#  possible to find the union, intersection, difference, symmetric difference, subset, 
# super set and disjoint set among sets.

# using set in python is like using Objects in javascript.....


# st = {'item1', 'item2', 'item3', 'item4'}
# st.update(['item5','item6','item7'])
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = ['tomato', 'potato', 'cabbage','onion', 'carrot']
# fruits.update(vegetables)
# print(fruits)
# print(type(fruits))

#convertimng lists to set

# lst = ['item1', 'item2', 'item3', 'item4', 'item1']
# stt = set(lst)
# print(stt)

# remove_fruit= fruits.pop
# print(remove_fruit)
import threading

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
find_length = len(it_companies)
print(find_length)

add_lst = it_companies.add("twitter")
srt_set = list(it_companies)
srt_set.sort()
print(srt_set)


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


named = age.count(24)
print(named)

# algo to to multiplay numbers in a list
def get_squared(numbers):
    get_number = []
    for n in numbers:
        get_number.append(n*n)
    return get_number

print(get_squared(age))


for n in range(len(age)):
    for j in range(n+1, len(age)):
        
        if age[n] == age[j]:
            print(age[n], "is a duplicate")
            break


my_info = ("tola", 31, "data engineer")

# unpacking

name,age,job = my_info

print(name)


# zip METHOD IN PYTHON


# names = ["Jenny", "Alexus", "Sam", "Grace"]
# heights = [61, 70, 67, 64]
# Combine = list(zip(names,heights))
# print(Combine)

# ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]


# # WHILE LOOP to output the same as the FOR loop

# length = len(ingredients)
# index = 0

# while index < length:
#     print(ingredients[index])
#     index += 1


# using for-loop with range on a list 
# for i in range(len(ingredients)):
#     # print(i)
#     if i <= 4:
#         print(ingredients[i], i)
    

# # using just for-loop on a list 
# for ing in ingredients:
#     print(ing)



# for i in range(10,0,-1):
#     print(i)


# python_topics = ["variables", "control flow", "loops", "modules", "classes"]


# for pyt in range(len(python_topics)):
#     if pyt < 4:
#         print("I am Learning", python_topics[pyt])


# for pyt in python_topics:
#     print(pyt)


items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

# look for red head band in the list using for LOOP 

for items in range(len(items_on_sale)):
    if items == 3:
        print(items_on_sale[items])
        break



print("Checking through the sale list....")



for items in items_on_sale:
    if items == "red headband":
        print(items)
        break


big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# print only the positive numbers 

for i in big_number_list:
    if i <= 0:
        continue
    print(i)