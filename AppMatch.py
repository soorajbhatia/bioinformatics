

def HammingDistance(Text,Text2):

###First is the Hamming Distance Function###

#defines variables to be used
    n = len(Text)
    z = 1
    j=0

#goes through both sequences and increments j by one every time there's a mismatch
    for l in range(n):

        MatchPattern1 = Text[l:l + z]
        MatchPattern2 = Text2[l:l + z]
        if MatchPattern1 != MatchPattern2:
            j = j + 1

#prints number of mismatches
    return(j)

###Here ends the Hamming distance Function###



#opens file specified in quotes
f= open("data1.txt")

#reads lines from files, program expects two lines with one sequence on each line
lines = f.readlines()
Text='TGAGTGGGGG' #must be entered manually, else causes program to crash
#print(Text)
Sequence=lines[1]

k = len(Text)
m = 5 #must be entered manually, else causes program to crash






#to find and create a list of mismatches with up to m SNPs
mismatches=[]

for i in range(len(Sequence) - m):
    Text2 = Sequence[i:i + k]
    HammingDist(Text,Text2)
    if HammingDist(Text,Text2) <= m:
        mismatches.append(Text2)
#print(mismatches)

#to find the position of the mismatched with up to m SNPs
def PatternIndex(IndexText, Indexk, IndexPattern):
    listy=[]
    n = len(IndexText)
    for i in range(n - Indexk + 1):
        MatchPattern = IndexText[i:i + Indexk]
        if MatchPattern == IndexPattern:
           # index = i
            listy.append(i)
    return(listy)

indexes=[]
for i in mismatches:
    #print(i)
    IndexText=Sequence
    Indexk=len(i)
    IndexPattern=i
   # for i in PatternIndex(IndexText, Indexk, IndexPattern):
    indexes.extend(PatternIndex(IndexText, Indexk, IndexPattern))
    #print(PatternIndex(IndexText, Indexk, IndexPattern))

#print(indexes)
almost = list(dict.fromkeys(indexes))

x = sorted(almost)
#print(x)
data = x
print(*data)
print(len(x))

