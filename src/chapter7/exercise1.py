while True:
    try:
        file_name=input("Enter file directory- ")
        file=open(f'{file_name}','r')
        break
    except:
        print("Couldn't open file:",file_name)
for line in file:
    print(line.upper())