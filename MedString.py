from itertools import permutations as p
import itertools

with open('data.txt', 'r') as file:
    k = int(file.readline())
    Dna = file.readlines()

#creates a list of all possible kmers


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


# Function which returns subset or r length from n 

def perm(n, seq):
    listy=[]
    for p in itertools.product(seq, repeat=n):
        listy.append("".join(p))
    return(listy)



#Finds median string

def MedianString(Dna, k):
    final=[]
    kmers = perm(k, "ATCG")
    for kmer in kmers:
        tosum=[]
        for string in Dna:
            minham=[]
            for i in range(len(string) - k + 1):
                pattern = string[i:i + k]
                Text = pattern
                minham.append(HammingDistance(kmer,Text))
            tosum.append(min(minham))
        final.append(sum(tosum))

    index = final.index(min(final))
    return(kmers[index])


print(MedianString(Dna,k))





