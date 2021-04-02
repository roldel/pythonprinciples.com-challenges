'''Consecutive zeros

The goal of this challenge is to analyze a binary string consisting of only zeros
and ones. Your code should find the biggest number of consecutive zeros in the string.
For example, given the string:

"1001101000110"

The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter,
which is the string of zeros and ones. Your function should return the number
described above.'''

def  consecutive_zeros(binary):
    
    #Max successive 0 counter
    maxcount = 0
    
    #Live counter for 0 inside the for loop
    count = 0
    
    for number in binary:
        #if loops meets a 0, starts counting
        if number == "0" :
            count += 1
            
            #Update maxcount value if a better 0s streak is met inside the for loop
            if count > maxcount :
                maxcount = count
        
        #Reset counter if number met is not a 0
        else:
            count = 0

    return maxcount  


