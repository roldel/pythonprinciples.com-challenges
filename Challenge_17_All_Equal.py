'''All equal

Define a function named all_equal that takes a list and checks whether all elements
in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.'''


def all_equal(items):
    
    # check if the items list is empty
    if len(items) >= 1:
        
        #Initialize 1st list item
        first = items[0]

        #Loop over remaining items (1st item removed via slice index)
        for item in items[1:]:
            if item != first :
                return False
    return True