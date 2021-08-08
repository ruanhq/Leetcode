#1864.

#111000:
#6: 0, 1, 2; -> 1
#3: 0, 2
#Just the difference between the 1 in the even index and the number of 1 in the odd index 
#010: 
#1110: 

def minSwaps(s):
    n = len(s)
    counterIndex = defaultdict(list)
    for i in range(n):
        if s[i] == 0:
            counterIndex[0].append(i)
        else:
            counterIndex[1].append(i)
    if (n % 2 == 0 and len(counterIndex[0]) != len(counterIndex[1])) or (n % 2 == 1 and abs(len(counterIndex[0]) - len(counterIndex[1])) != 1 ):
        return False
    else:
        oddCount = 0
        evenCount = 0
        for j in counterIndex[1]:
            if j % 2 == 0:
                evenCount += 1
            else:
                oddCount += 1
        return abs(oddCount - eventCount)


1, 4 -> 

1111000 ->  



#To calculate the required number of modifications from the array to the alternated version.
#
#
def calc(alter):
    res = 0
    for c in s:
        if c != alter:
            res += 1
        alter = "1" if alter == "0" else "0"
    return res // 2

#CNN: we have a filter to scan through the pixels with point-wise dot product for each of the filter
#and then the filter moves spatially to traverse the image.
#It mainly capture the spatial dependence across pixels in the image.

#scanning the values through the pixels by point-wise product.






#it 

#Difference between RF and GBDT: sequential 


#we build a bi-directional LSTM model here.

#Attention/ max-pooling/ : sample-based discretization process, 
#scanning through the pixels with a certain stride.

#downsampling(select the maximum 

#For each of the region represents by the filter, we take the maximum of that region.

#Select the maximum pixel value for each of the batch(where the filters scans through the
#pixels)
#maxpooling select -> reduce the size of the output size, we have a filter, stride -> by how many steps
#it slides across the pixels 
#zero padding:
#Describe a situation where you strongly disagree with your colleague:

#I still remember a situation where one of my colleague , but I thought we should 
#definitely made it to earn trust of our business partners.

#average 
#AUC: 
#What's the variance inflation factor?
#What's the 
#LSTMs are sensitive to different random weight initializations.
#Dropout is much harder to implement in LSTMs
#LSTMs are easy to overfit.
#LSTMs require more memory to train.
#Reduce overfitting: data augmentation(flip the image, reverse the image, add noise on top of the image), dropout, l1/l2 regularization, 
#data augmentation -> 
#distributed sampling, cache event, 

#How to design a CNN? 
#How to design a RNN?
#How to design a LSTM?
#How to design a RNN?
Why the linear model not suitable for classification? 
dropout randomly remove some of the weights(connections) out by a certain probability p.
#drop a unit out, simulates a sparse activation from a given layer, which
#interestingly, in turn, encourages the network to actually learn a sparse
#representation as a side-effect.
#activation of the hidden units become sparse(artificially perturb and simplify the model here)
#In very large neural networks, 

#背一遍BQ
#背一遍八股文
#背一遍项目









































