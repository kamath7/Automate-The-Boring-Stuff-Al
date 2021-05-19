import logging
logging.basicConfig(filename = 'my_lalle_logs.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) #disable logs
'''
5 levels of logging
INFO
WARNING
CRITICAL
DEBUG
ERROR
'''
logging.debug('Starting')
def factorial(n):
    logging.debug('Start of factorial {0}'.format(n,))
    total = 1
    for i in range (1,n+1):
        total *=i
        logging.debug('Value of is is {0}. Value of total is {1}'.format(i, total,))
    return total 

print(factorial(5))
logging.debug('end')