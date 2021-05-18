import os 
for folderName, subFolders, filenames in os.walk('C:\\Users\\Ganesh\\Desktop\\Automate the Boring Stuff\\Files\\lalleFolder'):
    print('The folder is {0}'.format(folderName,))
    print('Subfolders in the folder {0} here are {1}'.format(folderName, subFolders,))
    print('Filenames here {0}'.format(filenames,))
