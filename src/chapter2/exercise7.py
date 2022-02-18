money = float(input('Enter amount of money to make change for: '))
dollar20 = money // 20
if dollar20 == 1:
    print(dollar20, 'twenty')
else:
    print(dollar20, 'twenties')

remainder1 = money % 20
dollar10 = remainder1 // 10
if dollar10 == 1:
    print(dollar10, 'ten')
else:
    print(dollar10, 'tens')

remainder2 = remainder1 % 10
dollar5 = remainder2 // 5
if dollar5 == 1:
    print(dollar5, 'five')
else:
    print(dollar5, 'fives')

remainder3 = remainder2 % 5
dollar1 = remainder3 // 1
if dollar1 == 1:
    print(dollar1, 'one')
else:
    print(dollar1, 'ones')

remainder4 = remainder3 % 1
quarter = remainder4 // 0.25
if quarter == 1:
    print(quarter, 'quarter')
else:
    print(quarter, 'quarters')

remainder5 = remainder4 % 0.25
dime = remainder5 // 0.1
if dime == 1:
    print(dime, 'dime')
else:
    print(dime, 'dimes')

remainder6 = remainder5 % 0.1
nickel = remainder6 // 0.05
if nickel == 1:
    print(nickel, 'nickel')
else:
    print(nickel, 'nickels')

remainder7 = remainder6 % 0.05
penny = remainder7 // 0.01
if penny == 1:
    print(penny, 'penny')
else:
    print(penny, 'pennies')