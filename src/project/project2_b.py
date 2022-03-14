#  function that checks and opens for the correct file input
# if incorrect, function displays error message and prompts for a correct input
def open_file():
    global measles_file
    while True:
        try:
            file = input('Enter the input file name: ')
            measles_file = open(f'{file}.txt', 'r')
            break
        except:
            print(f"Couldn't open the file: {file}\nPlease try again")
# function that performs the checking of the users criteria and processes it
def process_file(file_object):
    # the message is displayed to instruct the user of the correct prompts
    message = '''
    Please enter a year and income level
    Note that for income level, the required input must be either "1, 2, 3 or 4" according to the following scheme:
    "1" for "low income"
    "2" for "lower middle income"
    "3" for "upper middle income"
    "4" for "high income"
    '''
    print(message)
    while True:
        #  the try-block that checks for a valid year input
        try:
            year = input('Please enter the year: ')
            income_level = input('Please enter the income level: ')
            int(year) and int(income_level)  # check whether input value is an integer
            # if blocks that define and check for the income_level input
            if income_level == '1':
                income_level = 'WB_LI'
            elif income_level == '2':
                income_level = 'WB_LMI'
            elif income_level == '3':
                income_level = 'WB_UMI'
            elif income_level == '4':
                income_level = 'WB_HI'
            else:
                print('Invalid input for income level, please try again')
                continue
            break
        except:
            print('Please type integer values for both year and income level')
    ls = []  # list appended to every %age according to the users criteria through which we check the count and the average
    max_percentage = 0
    min_percentage = 100
    for line in file_object: # to read through each line of the file and find out the users criteria
        line1 = line.split()
        if line1[-1].startswith(year) and line1[1].startswith(income_level):
            ls.append(int(line1[2]))
            # compare the line :"Afghanistan                                        WB_LI    0 Eastern Mediterranean"     1981
            # if block that checks if the percentage in the line is greater than "0"
            if int(line1[2]) > max_percentage:
                max_percentage = int(line1[2])  # the percentage now becomes the maximum percentage
                max_country = line1[0]  # the country of the respective percentage
            # if block that checks if the percentage in the line is less than "100"
            if int(line1[2]) < min_percentage:
                min_percentage = int(line1[2])  # it now becomes the minimum percentage
                min_country = line1[0]  # the country of the respective percentage
    # if block to check if the year appears in the file
    if len(ls) == 0:  # in case the list "ls" is empty
        print('The given year is not in the selected file')
    else:
        print(f'Count: {len(ls)}\nAverage percentage of children vaccinated: {sum(ls) / len(ls)}')
        print(f'The country with the highest percentage is {max_country} having {max_percentage}%')
        print(f'The country with the lowest percentage is {min_country} having {min_percentage}%')
        file_object.close()
# defining the main function that calls upon both the open_file and process_file functions
def main():
    open_file()
    process_file(measles_file)

main()   # then we call the main function to execute the whole program