#254 Factor Combinations:

import math
class Solution:
    def backtracking(self, n, ans, curr, start):
        if len(curr) > 0:
            curr.append(n)
            ans.append(curr[:])
            curr.pop()
        for i in range(start, int(math.sqrt(n)) + 1):
            #satisfying the condition to go one layer deeper, then add the value onto the current sequence(iterate through the next layer) before pop them out
            if n % i == 0:
                curr.append(i)
                #now start from the current i:
                self.backtracking(n//i, ans, curr, i)
                curr.pop()
        
    def getFactors(self, n: int) -> List[List[int]]:
        result = []
        self.backtracking(n, result, [], 2)
        return result

class Solution:
    def backtracking(self, n, ans, curr, start):
        if len(curr) > 0:
            curr.append(n)
            ans.append(curr[:])
            curr.pop()
        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                curr.append(i)
                self.backtracking(n // i, ans, curr, i)
                curr.pop()
    def getFactors(self, n: int):
        result = []
        self.backtracking(n, result, [], 2)
        return result


class Solution:
    def backtracking(self, n, ans, curr, start):
        if len(curr) > 0:
            curr.append(n)
            ans.append(curr[:])
            curr.pop()
        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                curr.append(i)
                self.backtracking(n//i, ans, curr, i)
                curr.pop()

    def getFactors(self, n: int) -> List[List[int]]:
        result = []
        self.backtracking(n, result, [], 2)
        return result


#pop them out -> whether it satisfies the condition to go one layer further deeper.

class Solution:
    def backtracking(self, n, ans, curr, start):
        if len(curr) > 0:
            curr.append(n)
            ans.append(curr[:])
            curr.pop()
        for i in range(start, int(math.sqrt(n)) + 1):
            



#talk about a past project and go into detail:
#how to find the standard deviation of the median?



def getEvenSum(num):
    i = 0
    curInd = 1 #1 means even, -1 means odd
    result = 0
    while i < len(num):
        if curInd == 1:
            result += num[i]
        i += 1
        curInd *= -1
    return result

num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
getEvenSum(num)

#how to evaluate whether we should build an office in China?

#talk about the causal effect of a training program, random 1000 students, 
#take top 100, bottom 100 we want to see the causal effect of the 
#training program?


#1. improvement -> because students are better or because of the training
#student profile would be a confounding variable here.

#2. variable selection: forward stepwise, backward elimination, 
#all subset regression, pca to reduce the dimension and perform the lasso here.

#simpson's paradox: subgroup trend vanishes in the total group or reversed.

#Esuggest to do a before and after comparison random selecting 
#200 students -> use paired t-tests statistic s.

#how to calculate standard error here.
#how to calculate the median?

#assume there are interactions between 
#different notification groups, decide whether there are 
#high quality or low quality users.

#-> dig deeper into different sub-groups here.

#how to improve the classification model?
#features -> precision/ recall -> how many ratio of actual notifications we have identified successfully?

#there maybe a trend in the subgroup but when you
#combine them then the trend disappear or reverse.
#I would suggest to do a before and after comparison by selecting random 200 students and compare them using t-test statistics.

#your model is about to roll out, -> iteratively optimize the model performance here
#no multicollinearity and another highly correlated variables occurs -> we didn't select this variable in feature selection here.

#generate(0, 1) -> generate(0, 0.8)
\
#Y ~ X1 + X2, Y ~ X1 + X3 -> X3 = X1 - X2

#azure machine learning DS team at Microsoft AI Platform here.

#Y ~ X1 + X2, Y ~ X1 + X3 -> X3 = X1 - X2

#there maybe a trend in the subgroup but when you combine them 
#together then the trend disappears or reverse.
#I would suggest to do a before and after, random select 200 of the total samples.


#It's different from Global Attention Model in a way that in Local attention model
#only a few positions from source(encoder) is used to calculate the 
#aligned weights a<t>, below is the diagram for the local attention model.

#It can be referred from the picture, first single-aligned position p<t> is 
#found then a window of words from source(encoder) layer along with h<t> is 
#used to calculate align weights: aligned weights depicts the amount of attention
#the past element paying attention to the word in the next level.

#Theoretically the self-attention can adopt any score functions above, but
#just replace the target sequence with the same input sequence.

#Transformer network is entirely built upon self-attention mechanisms without
#using recurrent network architecture ->

#input embedding with positional encoding -> multihead attention 
#-> add/normalization -> feed forward network -> add/normalization layer(dropout)(can be seen as a form of regularization methodology here)

#multi-head attention: linear, linear, linear -> scaled dot-product attention here.

#scaled dot-product 
#concat -> linear -> 

#电商骗贷, 骗贷成本低, 恶意引导 -> group collaborative fraud, grouping fraud like these.

#卖家入驻，内外勾结.

Collaborative behaviors, complex/ compound rules combining them together.
the identities are independent to each other and it's hard to find the relationships between them.

Automatic rule engine, unsupervised learning rule engine, rule engine

Global Paypal working capital(PPWC) (multi B$ small business lending product)
data driven automated underwriting, credit risk management, lead first party fraud strategy development
-> strategy development here.

#design the risk architecture to merge two risk engines for smooth migration purpose.
#build the international risk management team and capability from the ground.

Global credit expansion(UK/DE market)
Third party bureau data integration -> realtime credit decision engine.

#white collar -> online merchants/ E-commerces

#payment industry here to evaluate the model here.

#transformers -> global credit expansion(UK/DE markets)
#third party bureau data integrations to the real-time credit decision engine here.

#group/ collaborative fraud, combining fraud like these.

#dive deep -> case study -> email sending -> how to detect where is the problem arising from?
#into different user segments here and comparing different levels of features to check 
#if there are major difference between them.

#comparisons here -> development of data pipeline ->
#rearrange across cores here and making comparison.

#similar to price change -> send email 

#creativity/ collaboration -> providing reasoncodes -> threshold we have a backup plan(adjust the threshold by ourselves)
#system design: notification system here.

#coding: given 2-d int array 0/1 seat available/taken -> looking for the k available categories

#What's the architecture of transformer?
#easy level leetcode:

#construct a leetcode here and, machine learning models, basics.




#the precision on the 95% recall:


df.join(df2, Seq(""))













