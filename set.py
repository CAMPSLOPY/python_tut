# Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. 
# The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements.
#  In Python set is used to store unique items, and it is
#  possible to find the union, intersection, difference, symmetric difference, subset, 
# super set and disjoint set among sets.

# using set in python is like using Objects in javascript.....


st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ['tomato', 'potato', 'cabbage','onion', 'carrot']
fruits.update(vegetables)
print(fruits)
print(type(fruits))

remove_fruit= fruits.pop
print(remove_fruit)

cool_number = 12 + 30
ak = cool_number * 5
print(cool_number)

print(ak)