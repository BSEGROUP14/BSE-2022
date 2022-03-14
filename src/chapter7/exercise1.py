while True:
    try:
        file_name = input("Enter file directory: ")
        file = open(f'{file_name}', 'r')
        break
    except:
        print(f"Couldn't open file: {file_name}\nPlease try again")
for line in file:
    print(line.upper())
file.close()