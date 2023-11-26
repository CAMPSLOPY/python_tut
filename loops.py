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




for n in range(0, 11):
    print(n)

count = 0
while count < 11:
    print(count)
    count = count + 1