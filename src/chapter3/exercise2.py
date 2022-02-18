try:
    hours = int(input('Enter hours: '))
    rate = float(input('Enter rate: '))

    if hours > 40:
        pay1 = (hours - 40) * rate * 1.5
        pay2 = (40 * rate) + pay1
        print('Pay :', pay2)
    else:
        pay = hours * rate
        print('Pay: ', pay)
except:
    print('Error, please enter numeric input')