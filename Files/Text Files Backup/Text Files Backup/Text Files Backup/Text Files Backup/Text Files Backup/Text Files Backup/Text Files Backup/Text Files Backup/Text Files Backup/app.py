#Starting Files 

import os 
print(os.listdir())
print(os.path.join('folder1','folder2','rgb.jpg')) #joins file
print(os.getcwd())
os.chdir('C:\\') #Change directory
print(os.getcwd())

print(os.path.abspath('app.py'))
print(os.path.relpath('C:\\','app.py'))

print(os.path.dirname('app.py'))
print(os.path.basename('app.py'))

print(os.path.exists('C:\\Windows'))
print(os.path.isfile('C:\\'))
print(os.path.isdir('C:\\Windows'))

print(os.path.getsize('C:\\Users\\Ganesh\\Downloads'))
# print(os.listdir('C:\\Users\\Ganesh\\Downloads'))
os.chdir('C:\\Users\\Ganesh\\Downloads')
for file1 in os.listdir('C:\\Users\\Ganesh\\Downloads'):
    print(file1, os.path.getsize(os.path.abspath(file1)))
