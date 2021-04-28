#Functions

def printYourName(name):
    print('Hello {0}'.format(name,))


printYourName('Kams')
printYourName('Ronaldo')

print('Cat', 'dog', sep='\t')

lalle = 15 #Globally scoped variable

def something():
    lalle1 = 16 #locally scoped
    print(lalle,lalle1)

something()
print(lalle, lalle1)