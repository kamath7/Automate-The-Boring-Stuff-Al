#Loops

spam = 0 

while spam < 5:
    print("Lalle bois")
    spam = spam + 1

name = ''
while name != 'Lalle':
    print('Enter correct name')
    name = input()
    if name == 'adi':
        break

spam1 = 0
while spam1 < 5:
    spam1 = spam1 +1
    if spam1 ==3:
        continue
    print('Spam is {0}'.format(str(spam1)))

#For loops
total =  0
for i in range(0,101):
    total = total + i
    
print(total)

for i in range  (0, 100, 1):
    print(i)
