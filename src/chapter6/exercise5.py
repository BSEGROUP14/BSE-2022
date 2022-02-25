str = 'X-DSPAM-Confidence: 0.8475 '
num = float(str.removeprefix('X-DSPAM-Confidence:'))
print(num)