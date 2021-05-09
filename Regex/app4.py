import re 

beginwithregex = re.compile(r'^Hello')
print(beginwithregex.search('Hello Kams!').group())
endswithRegex = re.compile(r'Kams!$')
print(endswithRegex.search('Hello Kams!').group())

allDigits = re.compile(r'^\d+$')
print(allDigits.search('2121212').group())
# print(allDigits.search('212121x2').group()) -> Wont work

atRegex = re.compile(r'.at')
print(atRegex.findall('cat fat mat chat boot dat'))

moreAtRegex = re.compile(r'.{1,2}at')
print(moreAtRegex.findall('cat fat mat chat boot dat'))

name ='First Name: Kams Last Name: 007'
nameReg = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameReg.findall(name))

someMoreReg = re.compile(r'<(.*?)>')
print(someMoreReg.findall('<Pass Away><Eat Dinner><Skiing>'))

vowelRegex = re.compile(r'[aeiou]',re.IGNORECASE)
print(vowelRegex.findall('Give me the vowels'))
