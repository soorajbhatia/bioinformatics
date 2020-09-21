#Given a collection of strings Dna and an integer d, a k-mer is a (k,d)-motif if it appears in every string from Dna with at most d mismatches. For example, the implanted 15-mer in the strings above represents a (15,4)-motif.


import sys
import argparse
import itertools

k=5
d=1

f = open("data1.txt")
lines = f.readlines()
seq1 = lines[1]
seq2 = lines[2]
seq3 = lines[3]
seq4 = lines[4]
seq5 = lines[5]
seq6 = lines[6]

seqlist = [seq1,seq2,seq3,seq4,seq5,seq6]



# possible arrangements of length k
from itertools import product
def arrangements(k):
    result = product('ACGT', repeat = k)
    result = map(list, result)
    words = []
    for item in result:
        word = ''
        for letter in item:
            word += letter
        words.append(word)
    return(words)

# Hamming distance
def HammingDistance(p, q):
    dist = 0
    if len(p) != len(q):
        return('strings have unequal length!')
    else:
        for i in range(len(p)):
            if p[i] != q[i]:
                dist += 1
        return(dist)

def Neighbors(pattern, d):
        if d == 0:
            return {pattern}
        if len(pattern) == 1:
            return {'A', 'C', 'G', 'T'}
        else:

            #obtain suffix
            suffix = pattern[1:len(pattern)]
            prefix = pattern[0]

            # recursive algorithm (repeat function for each suffix)
            suffixNeighbors = Neighbors(suffix, d)

            # eligible neighbors
            neighborsList = arrangements(len(suffix))
            eligibleList = []
            for neighbor in neighborsList:
                hamming = HammingDistance(suffix, neighbor)
                if hamming <= d and neighbor not in eligibleList:
                    eligibleList.append(neighbor)

            # concatenate prefix to eligible neighbors of suffix
            finalList = []
            for item in eligibleList:
                newItem = prefix + item
                if newItem not in finalList:
                    finalList.append(newItem)

            # concatenate A, C, T, G to suffix itself
            nucleotides = ['A', 'C', 'G', 'T']
            for nucleotide in nucleotides:
                newItem = nucleotide + suffix
                if newItem not in finalList:
                    finalList.append(newItem)

        #finalList = ' '.join(str(item) for item in finalList)
        return(finalList)



j=0
while j < len(seqlist):
    
    seqlist[j] = seqlist[j].strip()
    j = j+1

metalist=[]
listytwo=[]
onelofl=[]
final=[]

for i in seqlist:
    listy=[]

    for l in range(len(i) - k + 1):
        pattern = i[l:l+k]
        listy.append(pattern)
    onelofl.append(listy)


fourlofl=[]
for i in onelofl:
    twolofl=[]
    threelofl=[]
    for j in i:
        twolofl.append(Neighbors(j,d)) 
    for thing in twolofl:
        for twothing in thing:
            threelofl.append(twothing)
    fourlofl.append(threelofl)
#print(fourlofl)


metalist = fourlofl


result = set(metalist[0])

for s in metalist[1:]:
    result.intersection_update(s)
print(result)

