# %%
person = {'name':"Jessa",
          "country":"USA",
          "telephone":11789}
print(person,type(person))
# %%
person = dict({'name':"Jessa",
          "country":"USA",
          "telephone":11789})
print(person,type(person))
# %%
person = dict([('name','mark'),('age',39),('number',612203)])
print(person,type(person))
# %%
sample_dict = {'name':'sai',10:'age'}
print(sample_dict,type(sample_dict))
# %%
person = {'name':'sai vardhan','age':24,'numbers':[1234,12345,1234567]}
print(person,type(person))
# %%
empty_dict = {}
print(type(empty_dict))
# %%
my_dict = {
    'a':10,
    'b':20,
    'c':30,
    'a':40
}
print(my_dict,type(my_dict))
# %%
my_dict = {
    'a':10,
    'b':20,
    'c':30,
    'a':40
}
print(my_dict['b'])
my_dict['b'] = 80
print(my_dict)
# %%
user = {'id':1,'age':30,'city':'USA'}
print(user['name'])
# %%
# %%
user = {'id':1,'age':30,'city':'USA'}
print(user.get('id'))
print(user.get('name'))
print(user.get('name','Unknown'))
print('age' in user)
print("name" not in user)
# %%
user = {'id':1,'age':30,'city':'USA'}
print(user.keys())
print(user.values())
print(user.items())
# %%
person = {"name": "Jessa", "country": "USA", "telephone": 1178}

# Iterating the dictionary using for-loop
print('key',':','value')
for key in person:
    print(key,':',person[key])
# using items() method
print('key', ':', 'value')
for key_value in person.items():
    print(key_value[0], key_value[1])
# %%
person = {"name": "Jessa", "country": "USA", "telephone": 1178}
print(len(person))
# %%
# %%
person = {"name": "Jessa", "country": "USA", "telephone": 1178}
person['weight'] = 50
person.update({'height':6})
print(person)
# %%
person = {"name": "Jessa", 'country': "USA"}
person.update({'weight':60,"height":6})
print(person)
# %%
person_details = {"name": "Jessa", "country": "USA", "telephone": 1178}

# set default value if key doesn't exists
person_details.setdefault('state','texas')
person_details.setdefault('zip')
person_details.setdefault("country","India")
for key,value in person_details.items():
    print(key,':',value)
# %%
person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}

# Remove last inserted item from the dictionary
deleted_item = person.popitem()
print(deleted_item)
print(person)
print()
deleted_item = person.pop('telephone')
print(deleted_item)
print(person)
print()
del person['weight']
print(person)
person.clear()
print(person)
del person
print(person)
# %%
dict1 = {'Jessa': 70, 'Arul': 80, 'Emma': 55}
dict2 = {'Kelly': 68, 'Harry': 50, 'Olivia': 66}
dict1.update(dict2)
print(dict1)
# %%
# address dictionary to store person address
address = {"state": "Texas", 'city': 'Houston'}

# dictionary to store person details with address as a nested dictionary
person = {'name': 'Jessa', 'company': 'Google', 'address': address}

# Display dictionary
print("person:", person)
print('city:',person['address']['city'])
for key,value in person.items():
    if key=='address':
        print("Person address")
        for nested_key,nested_value in value.items():
            print(nested_key,':',nested_value)
    else:
        print(key,':',value)       
# %%
# each dictionary will store data of a single student
jessa = {'name': 'Jessa', 'state': 'Texas', 'city': 'Houston', 'marks': 75}
emma = {'name': 'Emma', 'state': 'Texas', 'city': 'Dallas', 'marks': 60}
kelly = {'name': 'Kelly', 'state': 'Texas', 'city': 'Austin', 'marks': 85}

# Outer dictionary to store all student dictionaries (nested dictionaries)
class_six = {'student1': jessa, 'student2': emma, 'student3': kelly}
# Get student3's name and mark
print("Student3 name:",class_six['student3']['name'])
print("Student3 name:",class_six['student3']['marks'])
for key,value in class_six.items():
    print(key)
    for nested_key,nested_value in value.items():
        print(nested_key,":",nested_value)
# %%
dict1 = {'c': 45, 'b': 95, 'a': 35}

# sorting dictionary by keys
print(sorted(dict1.items()))
# Output [('a', 35), ('b', 95), ('c', 45)]

# sort dict eys
print(sorted(dict1))
# output ['a', 'b', 'c']

# sort dictionary values
print(sorted(dict1.values()))
# output [35, 45, 95]
# %%
numbers = [1,2,3,4,5]
even_squares = {x:x**2 for x in numbers if x%2==0}
print(even_squares)
# %%
