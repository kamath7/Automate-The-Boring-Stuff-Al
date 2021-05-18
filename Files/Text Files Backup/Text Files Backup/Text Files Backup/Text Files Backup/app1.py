lallefile = open('./lalle.txt',mode='w+')
# print(lallefile.read())
lallefile.write('I love watching King of the Hill')
print(lallefile.readlines())

lallefile.close()

lallefile = open('./lalle.txt',mode='a')
lallefile.write('My fav movies are Usual Suspects and Fight Club')
lallefile.close()

import shelve
shelfFile = shelve.open('lalle')
shelfFile['cars'] = ['Mustang','Porsche','Ferrari','Mercedes']
shelfFile.close()

shelfFile = shelve.open('lalle')
print(shelfFile['cars'])
print(list(shelfFile.keys()))