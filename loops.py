person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    print(key)
    if key == 'skills':
        for skill in person['skills']:
            print(skill)




# for n in range(0, 11):
#     print(n)

# count = 0
# while count < 11:
#     print(count)
#     count = count + 1


# for n in range(1, 8):
#     if n <= 8:
#         print(" # " * 8)


# for n in range(11, 0, -1):
#     print(n)

# count = 11
# while count > -1:
#     print(count)
#     count = count - 1

# for n in range(0, 11):
#     print(n * n)




# IDE =  ['Python', 'Numpy','Pandas','Django', 'Flask']

# for i in IDE:
#     print(i)

# Iterate 0 - 100  and print only even numbers

#  if n % 2 == 0:
# print even numbers

for n in range(0,101):
    if n % 2 == 0:
        addit = []
        print(n, "is an even number in the loop")

for x in range(0, 100):
    if x % 2:
        print(x, "is an odd number in the loop")