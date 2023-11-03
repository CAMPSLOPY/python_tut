# A tuple is a collection of different data types which is 
# ordered and unchangeable (immutable). Tuples are written with round brackets, ().
#  Once a tuple is created, we cannot change its values. We cannot use add, insert,
#  remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple
# operator: to join two or more tuples and to create a new tuple

mars = ("age", 50, 0.5,"50")
chan_mars = list(mars)
chan_mars[0] = "messi"
new_mars= tuple(chan_mars)


if "50" in new_mars:
    print("true")
else:
    print("False")
#  to delete an entire tuple 
del new_mars


# EXCERCISE DAY 6 

BM = ()
brother = ("josh")
sister = (" jane ")
mom = (" hally ")
father = (" sam ")
siblings = brother + sister + father + mom
family_members = ("brother", "sister", "father", "mom")
(bro, sis, *parent) = family_members
print(parent)

dad = list(family_members)
print(dad)


food_stuff_tp = ("Apple", "Mango", "Avocado","lettuce", "beef","chicken","bread")
food_stuff_lt = list(food_stuff_tp)

mid_tp = len(food_stuff_lt) // 2 
mid_tp_index_val = food_stuff_lt[mid_tp]

# get the length of the entire list
n = len(food_stuff_lt)

# if the middle item is an even number then calculate both figures and then divide by 2
if n % 2 == 0:
    # find the first middle item in the list
    mid1 = food_stuff_lt[n // 2 -1]
    # find the second middle item in the list
    mid2 = food_stuff_lt[n // 2]
    # add the two items together and then divide by to find the middle item
    midpoint = (mid1 + mid2) / 2
    print(midpoint)

    # if the item is an odd number then print the item
else:
    mid3 = food_stuff_lt[n // 2]
    print(mid3)




