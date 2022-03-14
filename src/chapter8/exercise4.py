while True:
    try:
        file_name = input('Enter file directory: ')
        file = open(f'{file_name}', 'r')
        break
    except:
        print(f"Couldn't open the file: {file_name}\nPlease try again")
ls = []
for line in file:
    line1 = line.split()
    for line_ in line1:
        if not line_ in ls:
            ls.append(line_)
ls.sort()
print(ls)
file.close()