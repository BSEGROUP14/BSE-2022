age = int(input('Enter age: '))
if age >= 18:
    print('You can vote.')
elif age >= 0:
    print('Too young to vote.')
else:
    print('You are a time traveller.')