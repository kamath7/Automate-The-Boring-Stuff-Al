import re 

namesRegex = re.compile(r'Lalle \w+')
print(namesRegex.findall('Lalle Nata, Lalle Rhea, Lalle Seere are gae'))
print(namesRegex.sub('Manku Tima','Lalle Nata, Lalle Rhea, Lalle Seere are gae'))

phoneReg = re.compile(r'''
\d\d\d #first string
-
\d\d\d #second string
-
\d\d\d\d''',re.VERBOSE)