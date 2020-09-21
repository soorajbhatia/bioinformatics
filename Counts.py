def mostCommon(lst): 
    from collections import Counter      
    return [Counter(col).most_common(1)[0][0] for col in zip(*lst)] 


def Counts(dna, k, t):
    import random
    import numpy as np
    lst = []
    motifs = []
    for string in dna:
        lstwo = []
        x = random.randint(0, len(string) - k - 1)
        pattern = string[x:x+k]
        motifs.append(pattern)

        j=0
        while j < len(pattern):
            lstwo.append(pattern[j])
            j += 1
        lst.append(lstwo)

    mostCommonLetters = mostCommon(lst)#finds most common letters in column

   # Score = 0 #not sure this does anything at all
    array = np.array(lst) #creates array of dna strings

    countarray = np.zeros((4,len(pattern))) #initializes array for profile
    mostCommonArray = np.array(mostCommonLetters)#turns most common letters list into array


    countsA = np.count_nonzero(array == 'A', axis =0)
    countsC = np.count_nonzero(array == 'C', axis =0)
    countsG = np.count_nonzero(array == 'G', axis =0)
    countsT = np.count_nonzero(array == 'T', axis =0)

    for column in range(len(pattern)):

        countarray[0,column] = (countsA[column])


    for column in range(len(pattern)):

        countarray[1,column] = (countsC[column])


    for column in range(len(pattern)):
        countarray[2,column] = (countsG[column])


    for column in range(len(pattern)):
        countarray[3,column] = (countsT[column])

    return(countarray)

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
'''seq6 = lines[6]
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
seq20 = lines[20]'''

dna = [seq1,seq2,seq3,seq4,seq5]

print(Counts(dna,k,t))


