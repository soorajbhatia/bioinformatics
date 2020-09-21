

def HammingDistance(Text,Text2):
#defines variables to be used
    n = len(Text)
    k = 1
    j=0

#goes through both sequences and increments j by one every time there's a mismatch
    for i in range(n):

        MatchPattern1 = Text[i:i + k]
        MatchPattern2 = Text2[i:i + k]
        if MatchPattern1 != MatchPattern2:
            j = j + 1

#prints number of mismatches
    return(j)

#opens file specified in quotes
#f= open("data.txt")

#reads lines from files, program expects two lines with one sequence on each line
#lines = f.readlines()
Text='ATA'#lines[0]
Text2='AAT' #lines[1]
print(HammingDistance(Text,Text2))
