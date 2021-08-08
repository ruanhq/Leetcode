#200. NumberOfIslands

class Solution(object):
    def numberOfIslaned(self, grids):
        if not grids or not grids[0]:
            return 0
        m = len(grids)
        n = len(grids[0])
        result = 0
        def searching(grids, i, j):
            if grids[i][j] == "0":
                return
            grids[i][j] = "0"
            if i != 0:
                searching(grids, i - 1, j)
            if i != m - 1:
                searching(grids, i + 1, j)
            if j != 0:
                searching(grids, i, j - 1)
            if j != 0:
                searching(grids, i, j + 1)
        for i in range(m):
            for j in range(n):
                if grids[i][j] == "1":
                    searching(grids, i, j)
                    result += 1
        return result


#map-reduce mechanism:
process and generate big data 
sets with a parallel, distributed algorithm or a cluster.

map: each worker node applies the map function to the
local data and writes the output to a temporary storage.
A master node ensures that only one copy of the redundant
input data is processed.

shuffle: worker nodes redistribute data based on the output
keys(produced by the map function),
such that all data belonging to one key is located on
the same worker node.

reduce: worker nodes now process each group of output data,
per key in parallel.




"""
reduce: worker nodes now process each group of output data,
per key in parallel.
map(k1, v1) -> list(k2, v2)
reduce(k2, list(v2)) -> list((k3, v3))

using U[0,1] -> generating U[0, 100]:


using U[0,1] -> generating U[0, 100] only when x > -1;


"""

#ML Concept answers and the 

Why overfitting?
The model learns the noise/ details on the training data to 
the extent that 

How to alleviate overfitting?


The model learns the noise/ details on the training data to 
the extent that it sacrifices the generalization ability -> 

The model learns the noise/ details on the training data to 
the extend that it sacrifices the generalization ability here.


It selects the maximum pixel value for each of the batch(where the 
    filters scans through the pixels)
maxpooling select -> reduce the size of the output size, we have a filter, stride 


The model learns 



















