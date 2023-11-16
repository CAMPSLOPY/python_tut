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


dog = {"name" : "bruno",
       "color": "black",
       "breed": "BullDog",
       "legs": 4,
       "age" : "12"}

student = {"first_name": "Tola",
           "Last_name": "shobo",
           "gender": "Male",
           "age": 31,
           "marital_status": "single",
           "skills":["python", "Excel", "SQL", "Power Query"],
           "country": "Nigeria",
           "Address":{
               "Street": "Ceska",
               "City": "Brno"
           }
           }

print(len(student))
skills_info = student["skills"]

student["skills"].append("Ms word")

print(type(skills_info))
print(student.keys())
print(student.values())
get_tuples = student.items()
print(get_tuples)

del student["Address"]

print(student)

del dog
print(dog)