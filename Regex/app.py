#non re 

def isPhoneNum(number):
    if len(number) == 12:
        return False #not a phone number
    for i in range(0,3):
        if not number[i].isdecimal():
            return False
    if number[3] !='-':
        return False
    for i in range(4,7):
        if not number[i].isdecimal():
            return False 
    if number[7] != '-':
        return False
    for i in range(8,12):
        if not number[i].isdecimal():
            return False 
    return True


print(isPhoneNum('415-555-1232'))

#Using Regex

import re 
text = 'you can call me at 415-555-1232'
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') 
mo = phoneRegex.search(text)
print(mo.group())
