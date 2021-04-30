#Range and lists

a = list(range(0,4))
print(a)

b = list(range(0,100,2))
print(b)

for i in range(0, len(b)):
    print (i)

ingredients = ['mustard','corn flour','maida','pepper powder']

for i in ingredients:
    print(i)

details = ['adithya','25','Adult']
name, age, isAdult = details 
print(name,age, isAdult)

#Augmented operators
lalle = 69
lalle += 1
print(lalle)