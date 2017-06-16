def odd_even():
    for count in range(1,2000):
        print("number is ", count)
        if(count %2 == 0):
            print("this number is even number")
        else:
            print("this number is odd number")



odd_even()


# multiply function

def multiply(list, num):
    new_list = []
    for var in list:
        new_list.append(var * num)
    return new_list


a = [2, 4, 10, 16]
b = multiply(a, 5)
print(b)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# def a(x, y):
#   print x, y
#
# def b(other, function, *args, **kwargs):
#   function(*args, **kwargs)
#   print other
#
# b('world', a, 'hello', 'dude')

# output
#
# hello dude
# world
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def layered_multiples(multipy, list, num):
    new_array = []
    multiply_fun = []
    multiply_fun = multiply(list, num)
    for var in multiply_fun:
        temp = []
        for count in range(0,var):
            temp.append(1)
        new_array.append(temp)


    return new_array



x = layered_multiples(multiply, [2,4,5],3)


print (x)
# # output
# [[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]