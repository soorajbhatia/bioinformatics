import random
from collections import Counter
import numpy as np
import math

k=15
t=20

f = open("data1.txt")
lines = f.readlines()
seq1 = lines[1]
seq2 = lines[2]
seq3 = lines[3]
seq4 = lines[4]
seq5 = lines[5]
seq6 = lines[6]
seq7 = lines[7]
seq8 = lines[8]
seq9 = lines[9]
seq10 = lines[10]
seq11 = lines[11]
seq12 = lines[12]
seq13 = lines[13]
seq14 = lines[14]
seq15 = lines[15]
seq16 = lines[16]
seq17 = lines[17]
seq18 = lines[18]
seq19 = lines[19]
seq20 = lines[20]

dna = [seq1,seq2,seq3,seq4,seq5,seq6,seq7,seq8,seq9,seq10,seq11,seq12,seq13,seq14,seq15,seq16,seq17,seq18,seq19,seq20]

#dna = [seq1]
#print(-math.log(.222,2))

def mostCommon(lst): 
          
    return [Counter(col).most_common(1)[0][0] for col in zip(*lst)] 

motifsone = []
lst = []
for string in dna:
    lstwo = []
    x = random.randint(0, len(string) - k - 1)
    pattern = string[x:x+k]
    motifsone.append(pattern)
    j=0
    while j < len(pattern):
        lstwo.append(pattern[j])
        j += 1
    lst.append(lstwo)
mostCommonLetters = mostCommon(lst)
Score = 0
array = np.array(lst)
profilearray = np.zeros((4,len(pattern)))

mostCommonArray = np.array(mostCommonLetters)
countsA = np.count_nonzero(array == 'A', axis =0)
countsC = np.count_nonzero(array == 'C', axis =0)
countsG = np.count_nonzero(array == 'G', axis =0)
countsT = np.count_nonzero(array == 'T', axis =0)
for column in range(len(pattern)):
    profilearray[0,column] = -(countsA[column] / t)*math.log(((countsA[column] + 1) / (t)), 2)
for column in range(len(pattern)):
    profilearray[1,column] = -(countsC[column] / t)*math.log(((countsC[column] + 1) / (t)), 2)
for column in range(len(pattern)):
    profilearray[2,column] = -(countsG[column] / t)*math.log(((countsG[column] + 1) / (t)), 2)
for column in range(len(pattern)):
    profilearray[3,column] = -(countsT[column] / t)*math.log(((countsT[column] + 1) / (t)), 2)
Score = np.sum(profilearray)

#FinalScore = [99999999999999999999999999999999]
finalMotifs=[]
i = 0
while i <= 1000:
    lst = []
    motifs = []
    for string in dna:
        lstwo = []
        x = random.randint(0, len(string) - k - 1)
        #print(x)
        pattern = string[x:x+k]
        motifs.append(pattern)
        #print(i)
        #print(motifs)
        #print(pattern)
        j=0
        while j < len(pattern):
            lstwo.append(pattern[j])
            j += 1
        lst.append(lstwo)
      # print(pattern)
    mostCommonLetters = mostCommon(lst)#finds most common letters in column

   # Score = 0 #not sure this does anything at all
    array = np.array(lst) #creates array of dna strings

    profilearray = np.zeros((4,len(pattern))) #initializes array of length for profile

    mostCommonArray = np.array(mostCommonLetters)#turns most common letters list into array


    countsA = np.count_nonzero(array == 'A', axis =0)
    countsC = np.count_nonzero(array == 'C', axis =0)
    countsG = np.count_nonzero(array == 'G', axis =0)
    countsT = np.count_nonzero(array == 'T', axis =0)

    for column in range(len(pattern)):
        profilearray[0,column] = -(countsA[column] / t)*math.log(((countsA[column] + 1) / (t)), 2)
    for column in range(len(pattern)):
        profilearray[1,column] = -(countsC[column] / t)*math.log(((countsC[column] + 1) / (t)), 2)
    for column in range(len(pattern)):
        profilearray[2,column] = -(countsG[column] / t)*math.log(((countsG[column] + 1) / (t)), 2)
    for column in range(len(pattern)):
        profilearray[3,column] = -(countsT[column] / t)*math.log(((countsT[column] + 1) / (t)), 2)


    FinalScore = np.sum(profilearray)

    if FinalScore < Score:
        Score = FinalScore
        print(Score)
        finalMotifs = motifs
    i = i + 1
#print(Score)

x=finalMotifs
print(*x)


'''The first is the one represented by the pseudocode, a random sequence set (from within the dna sequence list) is selected and assigned as the "best set" and scored. A while loop is then started, a profile is then created from the "best set" and a new set of motifs assigned based on this profile - this assignment is based on probability so remember pseudocounts and remember to multiply not add. This new set is then scored. The new set score and current best set scores are then compared, if the new set is better, then the new set becomes the best set. The while loop then repeats. The while loop however breaks if the current best set has a better score than the new set. Once the while loop breaks, the function returns a set of Kmers. '''

