while True:
    try:  # trying to open the file so that in case it fails, the program will break out of the entire loop and execute nothing
        measles_file = open('measles.txt', 'r')
    except:
        print('Failed to open measles.txt file, please check your file directory and try running the program again')
        break
    output = input('Enter the output file name: ')
    output_file = open(f'{output}.txt', 'w')  # creating a file or erasing an existing file that it's going to write on
    print('Enter a year for cases on that particular year or enter "All" for cases on all years')
    while True:
        try:
            year = input('>')
            int(year)    # trying to see if the user entered an integer value
            for line in measles_file:   # reading the measles_file and writing specified data on the output_file
                line1 = line.split()
                if line1[-1].startswith(year):
                    output_file.write(line)
            break
        except:  # in case the user entered a non-integer value
            if year.lower() == 'all' or year == "":
                for line in measles_file:  # reading the measles_file and writing all data on the output_file
                    output_file.write(line)
                break
            else:
                print('Error, must be numeric input, please try again')
                continue
    measles_file.close()
    output_file.close()
    break  # to avoid repetition of the whole program since it is all under a while loop