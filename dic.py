# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

person["skills"][4] = "PHP"


# The Key() method returns the result from the dictionary as a list

#  Values() Returns the key values in the dictionary as a List.
print(person.values())
# print(person)