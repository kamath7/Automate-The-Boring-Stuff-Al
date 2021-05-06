# Repetition in a pattern
import re
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The lalle Batman and his sidekick Batwoman')
print(mo.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('Phone 690-690-1234')
print(mo1.group())

mo2 = phoneRegex.search('Phone 690-1234')
print(mo2.group())

batRegex = re.compile(r'Bat(wo)*man') #wo can appear as many times


batRegex = re.compile(r'Bat(wo)+man') #Wo required to appear one or more time
print(batRegex.search('Lalle Batwoman Batwowowoman').group())

regex = re.compile(r'\+\*\?') #to use special characters 

haReg = re.compile(r'(Ha){3}')
print(haReg.search('It was hilarious HaHaHa').group())

haha = re.compile(r'(Ha){3,5}')
print(haha.search('Lalle HaHaHa').group())

digitRegex = re.compile(r'(\d){3,5}')
print(digitRegex.search('my num is 1234567890').group()) #does greedy match. Matches the longest possible string

#non greedy
digitRegex = re.compile(r'(\d){3,5}?')
print(digitRegex.search('my num is 1234567890').group()) #returns 123 