#Some string methods


my_str2 = 'it\'s a lonely world'
print(my_str2.lower())
print(my_str2.upper())
my_str2 = my_str2.lower()
print(my_str2.islower())

#Others
print('good'.isalpha())
print('good123'.isalnum())
print('123.5'.isdecimal())
print(' '.isspace())
print('lets dance'.title())
print('lets dance'.startswith('l')) #Case sensitive
print('hello world'.endswith('world'))
print(''.join(['a','d','i']))
print('i love paneer butter masala'.split(' '))
print('Hello'.rjust(10)) #adds space
print('Hello'.ljust(10))
print('World'.center(20,'-'))
print('Hello'.rjust(10).strip())
print('Helloollehhello'.strip('ellho'))
print('Hello it\'s Kams'.replace('Kams','Ronaldo'))