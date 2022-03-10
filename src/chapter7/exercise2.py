while True:
    file_name = input('Enter file directory: ')
    try:
        file = open(f'{file_name}','r')
        break
    except:
        print(" couldn't open the file",file_name)
total = 0
count = 0
for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
           new_line=line.strip('\n') and float(line.strip('X-DSPAM Confidence'))
           total+=new_line
           count+=1
print('Average spam confidence: ', total / count)