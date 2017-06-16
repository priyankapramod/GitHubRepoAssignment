# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.
# Part II
# Modify the function above. Allow a list containing integers and strings
# to be passed to the draw_stars() function. When a string is passed, instead of displaying *,
# display the first letter of the string according to the example below. You may use the .lower()
# string method for this part.



x = [4, 6, 1, 3, 5, 7, 25]
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]



def stars(list):
    count = 0
    for var in list:
        for count in range(0, var):
            print("*", end=" ")
        print("\n")

stars(x)

print("end of first function")

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def stars_modify(list):
    coun = 0
    for var in list:
        if type(var) == int:
            for count in range(0, var):
                print("*", end=" ")
            print("\n")
        elif type(var) == str:
            for x in range(0, len(var)):
                print(var[0], end=" ")
            print("\n")
stars_modify(y)