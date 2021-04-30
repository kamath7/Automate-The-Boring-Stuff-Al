#Lists and Strings 

print ('a' in 'adithya')

#Difference - List - mutable and string - immutable

name = 'Kams'
# name[0] = 'L' #TypeError

#Hard copy vs Soft Copy
#References
lalle1 = [1,2,3]
lalle2 = lalle1

lalle2[0] = 20
print(lalle1, lalle2)

#Deep Copy
import copy
lalle2 = copy.deepcopy(lalle1)
lalle2[1] = 'something'
print(lalle1,lalle2)