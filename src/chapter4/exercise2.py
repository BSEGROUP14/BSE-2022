try:
    C = float(input('Enter initial amount of investment: '))
    r = float(input('Enter yearly rate of interest: '))
    t = float(input('Enter number of years until maturation: '))
    n = float(input('Enter number of times the interest is compunded per year: '))


    def invest(C, r, t, n):
        p = C * (1 + r / n) ** (t * n)
        print('Final value of investment=', round(p, 2))


    invest(C, r, t, n)
    invest(1000, 0.01, 1, 1)
except:
    print('Invalid input')