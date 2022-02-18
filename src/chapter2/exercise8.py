C = float(input('Enter initial amount of investment: '))
r = float(input('Enter yearly interest rate: '))
e = float(input('Enter number of years until maturation: '))
n = float(input('Enter number of times the interest is compounded per year: '))

p = C * (1 + r/n)**e
print('Final value of investment=',round(p,2))