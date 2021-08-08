#Python k-fold cross-validation implementation:
from random import seed
from random import randrange
def crossValidationSplit(dataset, folds = 5):
    datasetSplit = list()
    datasetCopy = list(dataset)
    #size of each fold:
    foldSize = int(len(dataset) / folds)
    for i in range(folds):
        fold = list()
        while len(fold) < foldSize:
            index = randrange(len(datasetCopy))
            fold.append(datasetCopy.pop(index))
        datasetSplit.append(fold)
    return datasetSplit


#randrange(100)
#We sample each observation in each of fold one by one.
for i in range(folds):
    fold = list()
    while len(fold) < foldSize:
        index = randrange(len(datasetCopy))
        fold.append(datasetCopy.pop(index))
    datasetSplit.append(fold)
return datasetSplit



from random import seed 
from random import randrange
def crossValidationSplit(dataset, folds = 5):
    datasetSplit = list()
    datasetCopy = list(dataset)
    foldSize = int(len(dataset)/ folds)
    for i in range(folds):
        fold = list()
        while len(fold) < foldSize:
        	#randomly select the index from the current list of observations:
            index = randrange(len(datasetCopy))
            fold.append(datasetCopy.pop(index))
    return datasetSplit


def crossValidationSplit(dataset, folds = 5):
	datasetSplit = list()
	datasetCopy = list(dataset)
	foldSize = int(len(dataset)/ folds)
	for i in range(folds):
	    fold = list()
	    while len(fold) < foldSize:
	    	#randomly select an index from the current list of observations.
	        index = randrange(len(datasetCopy))
	        fold.append(datasetCopy.pop(index))
	return datasetSplit



def crossValidationSplit(dataset, folds = 5):
	#return the list of observations.
    datasetSplit = list()
    datasetCopy = list(dataset)
    foldSize = int(len(dataset)/ folds)
    for i in range(folds):
        fold = list()
        while len(fold) < foldSize:
            index = randrange(len(datasetCopy))
            fold.append(datasetCopy.pop(index))
    return datasetSplit




#
np.vstack(f1)
np.stack(f1, axis = 0)
np.stack(f1, axis = 1)
imbalanced dataset, AUC, ROC, PR, F1-score

###
#of these two conversions, the ability to convert an FC layer
#to a CONV layer is a particularly useful in practice,
#consider a convNet architecture that takes a. 224 * 224 * 3 image,
#-> this is done by use of 5 pooling layers that downsample the input
#spatially by a factor of two each time, making the final spatial size
#224/32 = 7

#replace the first FC layer that looks at [7 * 7 * 512]




Input -> [[Conv -> RELU] * N -> Pooling?] * M -> [FC -> RELU] * K -> FC
Input -> [Conv -> Relu -> Conv -> Relu -> Pool] * 3 -> [FC -> RELU] * 2 -> FC
#FC: fully-connected layer
#FC: fully-connected layer, fully-connected layer, 

Input -> [Conv -> Relu -> Conv -> Relu -> Pool] * 3 -> [FC -> Relu] * 2 -> FC
#Ends by a fully-connected layer here.









































    