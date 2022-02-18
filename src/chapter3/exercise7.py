try:
    location = input('Enter location: ')
    pay = int(input('Enter amount of salary: '))

    if location == 'Mbarara' and pay > 4000000:
        print("Yes, I'll take the job")
    elif location == 'Mbarara' and pay <= 4000000:
        print('No thanks, I can find something better')
    elif location == 'Kampala' and pay >= 10000000:
        print("Yes, I'll take the job")
    elif location == 'Kampala' and pay < 10000000:
        print('No way!')
    elif location == 'Space':
        print("Without a doubt, I'll take it")
    elif pay >= 6000000:
        print("Sure, I can work with this")
    elif pay < 6000000:
        print('No, thanks!')

except:
    print('Invalid input')