while True:
    try:
        file_name = input('Enter file directory: ')
        file = open(f'{file_name}','r')
        break
    except:
        print("Couldn't open the file: ", file_name)
ls = []
for line in file:
    line1 =line.split()
    for line in line1:
        if not line in ls:
            ls.append(line)
ls.sort()
print(ls)