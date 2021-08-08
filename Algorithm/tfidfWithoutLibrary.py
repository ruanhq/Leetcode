#Coding-TFIDF without using any libraries:

#sum(residual) / sum(previousProb * (1 - previousProb))

corpus = [
         'this is the first document',
         'this document is the second document',
         'and this is the third one',
         'is this the first document',
         'this the fdo adsfpoajp naprefnajpc adf ss',
         'j asd aef jaf dfas erjpitu gaeuhoi gou',
         'ehqrui zadhfuo ahufog ahefui huiafe aio hnegij',
         'huifd aui hreui aui hreui hreuia aurfm djfic',
         'eraui nbvh abdhj xbhu heura uisc ustc pku'
         ]
sentence = []
for i in range(len(corpus)):
    sentence.append(corpus[i].split(' '))


def IDF(corpus, uniqueWords):
    idfDict = {}
    n = len(corpus)
    for i in uniqueWords:
        count = 0
        for sen in corpus:
            if i in sen.split(" "):
                count += 1
            idfDict[i] = (math.log((1 + n)/ (count + 1))) + 1
    return idfDict

wordFreq = {}
for i in range(len(corpus)):
    sentence = corpus[i].split(' ')
    for word in sentence:
        try:
            wordFreq[word].add(i)
        except:
            wordFreq[word] = {i}

#1988 Age: 33.
for word in wordFreq:
    wordFreq[word] = len(wordFreq[word])

def ComputeIDF(wordFreq):
    idfDict = {}
    for word in wordFreq:
        idfDict[word] = math.log(len(sentence) / wordFreq[word])
    return idfDict


#3-day delivery guarantee service: build a model to predict
#whether an order would be delivered on time.

#What features/ variables would you build?


#
SELECT A1.user_id, A1.email1, A2.email2
FROM 
(SELECT user_id, email AS email1) A1
JOIN 
(SELECT user_id, email AS email2) A2
USING(user_id)
WHERE A1.email1 < A2.email2;
#Typical types of fraud lists:


term frequency -> inverse document frequency: 

term-frequency: the number of times a term occurs in document / total numbers of terms in the document
inverse document frequency: number of documents/ number of documents where the term occurs

number of times a term occurs in a document / total number of terms in a document * log()


number of times a term occurs in a document/  total number of terms in a document 
















