/*
5.9.3.3 Estimating the Shapley Value
All possible coalitions (sets) of feature values have to be evaluated with and without the j-th feature to calculate the exact Shapley value. For more than a few features, the exact solution to this problem becomes problematic as the number of possible coalitions exponentially increases as more features are added. Strumbelj et al. (2014)43 propose an approximation with Monte-Carlo sampling:
where  
  is the prediction for x, but with a random number of feature values replaced by feature values from a random data point z, except for the respective value of feature j. The x-vector  
  is almost identical to  
 , but the value  
  is also taken from the sampled z. Each of these M new instances is a kind of "Frankenstein Monster" assembled from two instances.
Approximate Shapley estimation for single feature value:
Output: Shapley value for the value of the j-th feature
Required: Number of iterations M, instance of interest x, feature index j, data matrix X, and machine learning model f
For all m = 1,...,M:
Draw random instance z from the data matrix X
Choose a random permutation o of the feature values
Order instance x:   
Order instance z:  
Construct two new instances
With feature j:   
Without feature j:  
Compute marginal contribution:  
Compute Shapley value as the average:  
First, select an instance of interest x, a feature j and the number of iterations M. For each iteration, a random instance z is selected from the data and a random order of the features is generated. Two new instances are created by combining values from the instance of interest x and the sample z. The instance  
  is the instance of interest, but all values in the order before feature j are replaced by feature values from the sample z. The instance  
 is the same as   , but in addition has feature j replaced by the value for feature j from the sample z. The difference in the prediction from the black box is computed:
All these differences are averaged and result in:
 

Averaging implicitly weighs samples by the probability distribution of X.

The procedure has to be repeated for each of the features to get all Shapley values.
Constructive feedback -> a constructive feedback -> about promotion 
*/
/*
list of window functions:
row_number(), dense_rank(), rank(), lag(), lead(), ntile(), limit, 
sum() -> cumulative sum.
*/