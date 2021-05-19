#Starting logging

# raise Exception('Random error message')

def boxPrint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception('Symbol needs to be a string of length 1')
    if (width < 2) or (height < 2):
        raise Exception('Width and height must be greater than 2')
    print(symbol * width)
    for i in range(height-2):
        print(symbol + (' '* int(width-2))+symbol)
    print(symbol * width)

boxPrint('$',100,7)    
# boxPrint('$',1,1) #Will raise an exception
# boxPrint('$$',10,7) #Will raise an exception
import traceback 
try:
    raise Exception('Lalle msg')
except:
    errFile = open('err_file.txt','a')
    errFile.write(traceback.format_exc())
    errFile.close()
    print('Traceback written into logs')

dict1 = {'l1':'green','l2':'orange','l3':'red'}

def switchLights(myDic):
    for key in myDic.keys():
        if myDic[key] == 'green':
            myDic[key] = 'orange'
        elif myDic[key] == 'orange':
            myDic[key] = 'red'
        elif myDic[key] == 'red':
            myDic[key] = 'green'
    assert 'red' in myDic.values(), 'Neither light is red. {0}'.format(myDic)     
switchLights(dict1)
print(dict1)