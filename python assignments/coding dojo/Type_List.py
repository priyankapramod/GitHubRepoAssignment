# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string.
# If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the array contains.
# If it contains only one type, print that type, otherwise, print 'mixed'.


def seperate_list_elements(input):
    sum = 0
    new_list = []
    isNum = False
    isStr = False
    for var in input:
        if isinstance(var, int) or isinstance(var, float):
            sum = sum + var
            isNum = True
        elif isinstance(var, str):
            new_list.append(var)
            isStr = True
    if (isNum == True) and (isStr == True):
        print("The list is of mixed type")
    elif (isNum == True):
        print("The list contains only numbers")
    else:
        print("The list contains only string words")

    print ("total sum : " , sum)
    print("new list with only strings from input list:" , new_list)



l = ['magical unicorns',19,'hello',98.98,'world']
seperate_list_elements(l)
print("***********end of the test**********")
l = [2,3,1,7,4,12]
seperate_list_elements(l)
print("***********end of the test**********")
l = ['magical','unicorns']
seperate_list_elements(l)
print("***********end of the test**********")

