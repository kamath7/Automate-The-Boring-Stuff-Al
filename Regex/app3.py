import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex.findall('my number is 910-789-2910 and my alternate number 890-238-1290'))

search_string = '2 onions, 3 green grams, 15 sodas, 11 packets lays'

items_regex = re.compile(r'\d+\s\w+')
print(items_regex.findall(search_string))

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Give me the vowels'))

consonRegex = re.compile(r'[^aeiouAEIOU]')
print(consonRegex.findall('Give me the non vowels'))
