#we create a get_login_function that accepts firstname, lastname 
#ID. It returns a system login name

def get_login_name(first,last,idnumber):
    #ge the first 3 letters of the first latter
    set1 = first[0:3]

    #get the first 3 letters of the last name
    set2 = last[0:3]

    #get the last 3 characters of the ID
    set3 = idnumber[-3 :]

    #lets put them together

    login_name = set1+set2+set3

    #lets return the login name
    return login_name

    


