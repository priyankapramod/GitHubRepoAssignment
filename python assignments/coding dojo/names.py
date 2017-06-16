
def full_name(list):
    for count in range(0, list.__len__()):
        print(list[count]["first_name"] , list[count]["last_name"] )
    # for var in list:
    #     print(var["first_name"] , var["last_name"])



students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

full_name(students)



def fullname_numChars(dictn):
    for var in dictn:
        
        for count in range(0, list.__len__()):
            print(list[count]["first_name"] , list[count]["last_name"] )






users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
