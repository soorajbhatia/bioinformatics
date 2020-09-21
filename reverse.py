# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    reversedString=[]
    index = len(Pattern) # calculate length of string and save in index
    while index > 0: 
        reversedString += Pattern[ index - 1 ] # save the value of str[index-1] in reverseString
        index = index - 1; # decrement index
    print(''.join(reversedString)); # reversed string


