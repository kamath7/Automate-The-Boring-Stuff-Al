#! python3

import pyperclip, re 

#regex for phone
phoneRegex = re.compile(r'''
((\d\d\d)|(\(\d\d\d\)))? #area code
(\s|-) #First sep
\d\d\d #first 3 digits 
- #separator
\d\d\d\d #last 4 dig
(((ext(\.)?\s|x)   #extension word bit 
(\d{2,5}))? #xtension number bit
''',re.VERBOSE)

emailRegex = re.compile(r'''
[a-zA-z0-9_.+]+ #name bit
@ #@symbol
[a-zA-z0-9_.+]+ #domain
''',re.VERBOSE)

text = pyperclip.paste()

extractedPhone = (phoneRegex.findall(text))
extractedEmail = emailRegex.findall(text)
print(extractedPhone,extractedEmail)