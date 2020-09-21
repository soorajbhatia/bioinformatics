def mostCommon(lst): 
    from collections import Counter      
    return [Counter(col).most_common(1)[0][0] for col in zip(*lst)] 


def Profile(dna, k, t):
    import random
    import numpy as np
    lst = []
    motifs = []
    for string in dna:
        lstwo = []
        x = random.randint(0, len(string) - k - 1)
        #print(x)
        pattern = string[x:x+k]
        motifs.append(pattern)
    #print(motifs)
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

    profilearray = np.zeros((4,len(pattern))) #initializes array for entropy
    prarray = np.zeros((4,len(pattern))) #initializes array for profile
    mostCommonArray = np.array(mostCommonLetters)#turns most common letters list into array


    countsA = np.count_nonzero(array == 'A', axis =0)
    countsC = np.count_nonzero(array == 'C', axis =0)
    countsG = np.count_nonzero(array == 'G', axis =0)
    countsT = np.count_nonzero(array == 'T', axis =0)

    for column in range(len(pattern)):
        prarray[0,column] = (countsA[column] / t)
       # profilearray[0,column] = -(countsA[column] / t)*math.log(((countsA[column] + 1) / (t)), 2)
    for column in range(len(pattern)):
        prarray[1,column] = (countsC[column] / t)
       # profilearray[1,column] = -(countsC[column] / t)*math.log(((countsC[column] + 1) / (t)), 2)
    for column in range(len(pattern)):
        prarray[2,column] = (countsG[column] / t)
        #profilearray[2,column] = -(countsG[column] / t)*math.log(((countsG[column] + 1) / (t)), 2)
    for column in range(len(pattern)):
        prarray[3,column] = (countsT[column] / t)
      #  profilearray[3,column] = -(countsT[column] / t)*math.log(((countsT[column] + 1) / (t)), 2)

    return(prarray)

f = open("data1.txt")
lines = f.readlines()
k=8
t=5



f = open("data.txt")
lines = f.readlines()
seq1 = lines[1]
seq2 = lines[2]
seq3 = lines[3]
seq4 = lines[4]
seq5 = lines[5]

dna = [seq1,seq2,seq3,seq4,seq5]

print(Profile(dna,k,t))

#profilearray = -(Profile(dna,k,t))*math.log(((countsT[column] + 1) / (t)), 2)
