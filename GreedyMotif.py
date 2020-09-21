import numpy as np

#function GreedyMotif expects a probability distribution array with rows defined as probabilities of finding base "letter" at location "j". Rows must be defined in the order ATCG.

#initializes lists used

#actual function
def GreedyMotif(text, k, arr):
    products = [] 
    listofpatterns=[]


#reads through sequence "text" sequentially and finds all kmers in "text"
    for i in range(len(text) - k + 1):
        pattern=text[i:i +k]
        listofpatterns.append(pattern) #appends kmers to list for calling purposes once max probability is found

        listy = [] #list initialized within loop to allow for calculation of probabliity of finding that kmer
        for j in range(len(pattern)):
            letter=pattern[j]
            if letter == 'A': #if you find an A in location 'j'
                pr = arr[0,j]
                listy.append(pr)
            if letter == 'C': #if you find a C in location 'j'
                pr = arr[1,j]
                listy.append(pr)
            if letter == 'G': #if you find a G in location 'j'
                pr = arr[2,j]
                listy.append(pr)
            if letter == 'T': #if you find a T in location 'j'
                pr = arr[3,j]
                listy.append(pr) #appends probabilities to listy list
        Pr = np.prod(listy) # finds product of all probabilties currently stored in list listy
        products.append(Pr) #appends product of probabilties to products list
    maxy = max(products) #finds max of products
    for l in products:
        if l == maxy:
            index = products.index(maxy) #finds index of maximum
    return(listofpatterns[index])

#opens file and reads text/sequence and k from file, probabity array must be entered manually
f = open("data1.txt")
lines = f.readlines()

text = lines[0]
thek = lines[1]
k = int(thek.strip())

arr = np.array([[0.263, 0.342, 0.211, 0.329, 0.224, 0.184, 0.289, 0.237, 0.184, 0.158, 0.158, 0.184, 0.316], [0.263, 0.276, 0.263, 0.224, 0.276, 0.25, 0.184, 0.289, 0.25, 0.263, 0.303, 0.184, 0.171], [0.263, 0.211, 0.197, 0.237, 0.303, 0.289, 0.276, 0.263, 0.316, 0.342, 0.342, 0.263, 0.263], [0.211, 0.171, 0.329, 0.211, 0.197, 0.276, 0.25, 0.211, 0.25, 0.237, 0.197, 0.368, 0.25]])

#calls and prints function output
print(GreedyMotif(text, k, arr))
