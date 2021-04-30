#List methods

lalle_arr = ['kams','bums','lambs','crumbs']
print(lalle_arr.index('lambs')) #Returns index

lalle_arr.append('coombs')
print(lalle_arr)

lalle_arr.insert(1,'joomba')
print(lalle_arr)

lalle_arr.remove('kams')
print(lalle_arr)

num_arr = [-8,29,0,23,-19,69,55]
num_arr.sort(reverse=True)
print(num_arr)

lalle_arr.append('Kams')
lalle_arr.append('Bums')
lalle_arr.append('Lambs')

lalle_arr.sort()
print(lalle_arr)
lalle_arr.sort(key=str.lower) #Sorting alphabetically
print(lalle_arr)