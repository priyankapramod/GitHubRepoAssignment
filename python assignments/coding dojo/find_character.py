# input
# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'


# output
# new_list = ['hello','world']


def find_string_with_char(list, char):
    count = 0
    length = list.__len__()
    new_list = []
    while(count < length):
        for var in list[count]:
            # print("list[count] is", list[count])
            if var == char:
                new_list.append(list[count])
                # print("count is ", count)
                break
        count = count +1
        # print("counter is" , count)
    return new_list



word_list = ['hello','world','my','name','is','Anna']
char = 'o'
char2 = 'h'
char3 = 'n'
char4 = 'y'
print("testing char 'o'", find_string_with_char(word_list, char))
print("testing char 'h'", find_string_with_char(word_list, char2))
print("testing char 'n'", find_string_with_char(word_list, char3))
print("testing char 'y'", find_string_with_char(word_list, char4))