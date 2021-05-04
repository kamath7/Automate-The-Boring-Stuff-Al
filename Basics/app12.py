#Dictionaries

my_dict = {'name':'Kams','age':25,'nationality':'Indian'}
print('My name is {0}'.format(my_dict['name'],))

some_other_dict = {0:'India',1:'Brazil',2: 'Argentina'}
print(some_other_dict)

#Comparing two same dictionaries
a_dict = {'name':'Kams','age':29,'nationality': 'Indian'}
b_dict = {'age':29,'nationality': 'Indian','name':'Kams'}
print(a_dict == b_dict) #Works?

print('name' in my_dict) #Checking if key exists in a dictionary
#Dictionaries are mutable
print(list(my_dict.keys()))
print(list(my_dict.items()))
print(list(my_dict.values()))

for k,v in my_dict.items():
    print(k,v)

if 'name' in my_dict.keys():
    print('Good')

print(my_dict.get('Name','John Doe')) #get - use it to check if a value exists else use the alternate in the second arguement
my_dict.setdefault('city','Mangalore')
print(my_dict)

#Lalle Program 

message = 'a quick brown fox jumped over the lazy dog'
count = {}

for letter in message.lower().replace(" ",""):
    count.setdefault(letter, 0)
    count[letter] = count[letter] + 1
print(count)