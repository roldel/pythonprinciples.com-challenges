'''Thousands separator

Write a function named format_number that takes a non-negative number as
its only parameter.

Your function should convert the number to a string and add commas as a
thousands separator.

For example, calling format_number(1000000) should return "1,000,000".'''



def format_number(number):

    #Converts number arg into a string
    strnumber = str(number)
    #Reverse the string
    revstr = strnumber[::-1]
    #Initiate iteraztion counter
    count = 0
    #Initiate new str to build
    newstr = ""

    #Iterate over the reverse string char
    for i in revstr:
        #Every 3 char, insert a comma
        if count == 3:
            newstr += ","
            #Reset counter
            count = 0
        
        #Add the char to the new string     
        newstr += i
        count +=1

    #Reverses the built string    
    revback = newstr[::-1]
    
    return revback
        
    