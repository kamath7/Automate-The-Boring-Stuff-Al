#Simple program

print('Welcome to the world. What is your name?\n')
myName = input()

print('Good to meet you {0}'.format(myName,))
print('What is your age?')
myAge = input()
print("You are currently {0}. You will turn {1} next year".format(myAge, str(int(myAge)+1)))
print(len(myName))

#Types

print(str(27) + ' years old')
