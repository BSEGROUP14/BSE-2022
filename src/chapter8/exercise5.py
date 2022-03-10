while True:
    try:
        file_name=input("Enter the file directory ")
        file=open(f'{file_name}','r')
        break
    except:
        print("Couldn't open file:",file_name)
count=0
for line in file:
    if line.startswith('From')
        line1=line.strip("\n") and line.strip()
        count+=1
        print(line1[1])
print('count:',count)