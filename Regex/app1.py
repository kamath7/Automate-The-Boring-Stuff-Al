import re 

my_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = my_regex.search('my phone number is 123-456-7890')
print(mo.group())
print(mo.group(1))

my_regex_2 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d')
mo1 = my_regex_2.search('my phone number is (123) 546-9020')
print(mo1.group())

batregex = re.compile(r'Bat(man|mobile|bat|grundy)')
mo3 = batregex.search('my Batmobile is awesome')
print(mo3.group())