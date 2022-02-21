total = 0
count = 0
while True:
    try:
        number = input('Please enter number: ')
        if number == 'done':
            print(total, count, total/count)
            break
        total = total + int(number)
        count = count + 1
    except:
        print('Invalid input')