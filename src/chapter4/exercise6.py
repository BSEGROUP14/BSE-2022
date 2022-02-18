try:
    time = float(input('Enter hours: '))
    rate = float(input('Enter rate: '))
    def computepay(a,b):
        if a > 40:
            rate1 = (a - 40) * b * 1.5
            pay2 = (40 * b) + rate1
            print('Pay: ', pay2)
        else:
            pay = a * b
            print('Pay: ', pay)
    computepay(time,rate)
except:
    print('Error, please enter numeric input')