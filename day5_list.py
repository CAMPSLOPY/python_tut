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


# find the middle number
mid = empty[len(empty)//2]

mid = len(empty)//2
mid_item = empty[mid]
# print last item in the index 
last = len(empty) - 1
last_item_index = last
last_item = empty[last_item_index]

mixed_data_types = ['tola',31,6.0,"single","brno"]
it_companies = [ "Facebook", "Google", "Microsoft","Apple","IBM","Oracle","Amazon"]
print(len(it_companies))
# print the first company 
first_comp = it_companies[0]
#find the middle company
middle_comp_index = len(it_companies) // 2
middle_comp = it_companies[middle_comp_index]


# this is to get the last company in the list 
last_comp_index = len(it_companies) - 1
last_comp =it_companies[last_comp_index]
it_companies[6] = "Adidas"

# insert a new company in the middle

find_middle_comp = len(it_companies)//2
it_companies[find_middle_comp] = "FeFundinfo"


to_Upper = it_companies[2]
x = it_companies.extend("£")
print(it_companies)

# check if a certain company exist in the List

does_exist = "Google" in it_companies

# xx = it_companies.sort()
it_companies.reverse()

a = slice(3)
b = it_companies[a]
print(it_companies)

# slice out the first three from the element 
ba = it_companies[0::3]
print(ba)

# slice out the last 3 from the list 
bc = it_companies[5::]
# slice the last 3 elements  from the list 
print(bc)
# slice out the middle IT company from the list 
bb = it_companies[::]

bd = len(it_companies)//2 
be = it_companies[bd]
bf = slice(be)

print(it_companies)


