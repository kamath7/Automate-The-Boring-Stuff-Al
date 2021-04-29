# Try-Except
def div1(num):
    try:
        return 69/num
    except ZeroDivisionError:
        print('Division by zero not possible you fool')


print(div1(69))
print(div1(23))
print(div1(7))
print(div1(0))

inp = input('How old is Spider-Man?')
try:
    if int(inp) > 0:
        print("Haha I don't know the age")
    else: 
        print("hAAA")
except ValueError:
    print("you need to enter a number")
