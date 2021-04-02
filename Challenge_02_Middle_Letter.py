'''Middle letter

Write a function named mid that takes a string as its parameter.
Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".'''

def mid(string):
    wordlen = len(string)
    if wordlen % 2 == 0 :
        return("")
    index = wordlen // 2
    return string[index]
        