try:
    people = int(input('Enter number of people: '))
    if people > 200:
        print('Cost: $20,000')
    elif people > 100:
        print('Cost: $15,000')
    elif people > 50:
        print('Cost: $10,000')
    elif people > 0:
        print('Cost: $4,000')
    else:
        print('Invalid input')
except:
    print('Invalid input')