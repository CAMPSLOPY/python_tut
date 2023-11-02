import statistics

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
ba = it_companies[::3]
print(ba)

# slice out the last 3 from the list 
bc = it_companies[5::]
# slice the last 3 elements  from the list 
print(bc)
# slice out the middle IT company from the list 

# remove the middle IT company from the list
bd = len(it_companies)//2 
b_middle = it_companies[bd]
bf = it_companies.remove(b_middle)

# remove the first item in the list of the tech companies
b_first_item_index = it_companies[0]
b_first_item = it_companies.remove(b_first_item_index)

# remove the last IT company from the list
# step - 1 get the index numerical value of the last element in the list 
last_it_comp = len(it_companies) - 1
# attach the numerical value to the it company to get the string value of the last element in the list
last_it_comp_index = it_companies[last_it_comp]
# final step- remove the last element in the list using the remove method
last_it_comp_remove = it_companies.remove(last_it_comp_index)

# remove all the items in the list
it_companies.clear()

# destroy the variable it_companies 
del it_companies

# Join the following lists
fullstack = []
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
fs = front_end + back_end
fullstack.extend(fs)
fullstack.insert(5,"Python")
fullstack.insert(6,"SQL")
print(fullstack)


# numerical cal

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# sort the list and find the min and max age.

# step - 1 sort the list
age_sort = ages.sort()
# step - 2 find the min
min_age = min(ages)
print(min_age)
max_age = max(ages)
print(max_age)
ages.append(min_age)
ages.append(max_age)
ages.sort()

# find the median age 
mid_age_index= len(ages) // 2
mid_age = ages[mid_age_index]
# or 

n = len(ages)

if n % 2 == 0:
    middle_1 = ages[n //2 -1]
    middle_2 = ages[n //2]
    median = (middle_1 + middle_2) / 2
else:
    median = ages[n // 2]

print(round(median))

# find average
average = statistics.mean(ages)
print(average)


# or another way to find the average 
xa = sum(ages)
x_len = len(ages)
average_2 = xa / x_len

print(average_2)

# find the age range

range_age = range(max_age - min_age)
print(range_age)

compa_1 = abs(min_age - average)
compa_2 = abs(max_age - average)
print(compa_1)
print(compa_2)

if compa_1 == compa_2:
    print("True")
else:
    print("False")

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]


ilu_index = len(countries) // 2
ilu_string_value = countries[ilu_index]
print(ilu_string_value)

# or

k = len(countries)

if k % 2 == 0:
    ilu_1 = countries[k // 2 -1]
    ilu_2 =  countries[k //2]
    calc_ilu = (ilu_1 + ilu_2) / 2
    
else:
    calc_ilu = countries[k // 2]

print(calc_ilu)

midpoint = len(countries) // 2

first_half = countries[:midpoint + 1]
second_half = countries[midpoint: - 1]
print(len(first_half))
print(len(second_half))

# using slice method to unpack a list
west = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_west = west[0:3:]
# scandic_countries = west[3::]


# Unpacking a list 
ch,ru,us,*scandic_countries = west
print(scandic_countries)