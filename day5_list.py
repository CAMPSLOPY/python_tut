fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] 


list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)

print(list1) 


empty = ['banana', 'orange', 'mango', 'lemon','lime','gun']
empty_len = len(empty)
print(empty_len)

mid = empty[len(empty)//2]

mid = len(empty)//2
mid_item = empty[mid]
# print last item in the index 
last = len(empty) - 1
last_item_index = last
last_item = empty[last_item_index]

mixed_data_types = [31]
print(last_item)