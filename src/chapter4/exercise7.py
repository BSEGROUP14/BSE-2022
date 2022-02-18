try:
    score = float(input('Enter score: '))
    def computegrade(a):
        if a > 1.0 or a < 0.0:
            print('Bad score')
        elif a >= 0.9:
            print('A')
        elif a >= 0.8:
            print('B')
        elif a >= 0.7:
            print('C')
        elif a >= 0.6:
            print('D')
        elif a < 0.6:
            print('F')
    computegrade(score)
except:
    print('Bad score')