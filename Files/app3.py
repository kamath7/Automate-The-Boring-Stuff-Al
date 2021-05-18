import os , shutil
print(os.getcwd())
print(os.unlink())#Deletes but doesn't delete if dir has files
print(shutil.rmtree('C:\\Users\\Ganesh\\Desktop\\Automate the Boring Stuff\\Files\\Text Files Backup'))

import send2trash

send2trash.send2trash('C:\\Users\\Ganesh\\Desktop\\Automate the Boring Stuff\\Files\\lalle2.txt')