while True:
    try:
        file_name = input("Enter the file directory: ")
        file = open(f'{file_name}', 'r')
        break
    except:
        print(f"Couldn't open file: {file_name}\nPlease try again")
count = 0
for line in file:
    if line.startswith('From '):
        line1 = line.split()
        count += 1
        print(line1[1])
print('Count:', count)
file.close()