while True:
    file_name = input('Enter file directory: ')
    if file_name.lower() == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        break
    try:
        file = open(f'{ file_name}', 'r')
    except:
        print(f"Couldn't open file: {file_name}\nPlease try again")
        continue
    total = 0
    count = 0
    for line in file:
        if line.startswith('X-DSPAM-Confidence:'):
            new_line = line.strip('\n') and float(line.strip('X-DSPAM Confidence: '))
            total += new_line
            count += 1
    print('Average spam confidence: ', total / count)
    print('Please try entering me "na na boo boo"')
file.close()