# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.
#
# Your program should be able to accept and compare two lists: list_one and list_two.
# If both lists are identical print "The lists are the same". If they are not identical print
# "The lists are not the same." Try the following test cases for lists one and two:

# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]


# list_1 = ['a', 'a', 'a', 'b']
# >>> list_2 = ['a', 'b', 'b', 'b', 'c']
# >>> sum(a != b for a, b in zip(list_1, list_2))
# 2
# >>> abs(len(list_1) - len(list_2))
# 1
# >>> difference = sum(a != b for a, b in zip(list_1, list_2))
# >>> difference += abs(len(list_1) - len(list_2))
# >>> difference
# 3



def compare_array(list1, list2):
    isSame = False
    difference = sum(a != b for a, b in zip(list1, list2))
    difference += abs(len(list1) - len(list2))

    if(difference >= 1):
        print("the two arrays are not same")
        return isSame
    elif (difference == 0):
        print("the two arrays are same")












# The sum() sums up True and False values;
# this works because Python's boolean type is a subclass of int and False equals 0, True equals 1.' \
#                          ' Thus, for each differing pair of elements, the True values produced by the != tests add up as 1s.




list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
compare_array(list_one, list_two)
print("*******end of test**********")

list_one = [1,2,5,6]
list_two = [1,2,5,6,5,3]
compare_array(list_one, list_two)
print("*******end of test**********")


list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
compare_array(list_one, list_two)
print("*******end of test**********")

#
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
compare_array(list_one, list_two)
print("*******end of test**********")