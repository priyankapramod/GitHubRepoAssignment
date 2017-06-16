words = "It's thanksgiving day. It's my birthday,too!"

#string.find(substring)
print (words.find("day"))
new_word = ""
#string.replace(old, new[, max])
print (words.replace( "day", "smonth"))



#,    to concatenate number and string while printing
# +    only for strings
x = [2,54,-2,7,12,98]
print ("Max value element : " , max(x))
print ("Min value element : " , min(x))



#first and last elements of a list
x = ["hello",2,54,-2,7,12,98,"world"]

print (" first element in the List : ", x[0])
print (" last element in the List : ", x[x.__len__()-1])

#new list with first and last elements
y = []
y.append(x[0])
y.append(x[x.__len__()-1])
print(y)

#New list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
p = sorted(x)
print(p)
y = []

y = p[0:5]
# y.extend(x[6:])

z = p[4:]
z[0] = y
print(z)


