ls = []
while True:
    try:
        number = input('Enter number: ')
        if number == 'done':
            print(min(ls), max(ls))
            break
        ls.append(int(number))
    except:
        print('Invalid input')