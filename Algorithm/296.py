#296. Best Meeting Points:
grids1 = [[[1, 0, 0, 0, 1], [0, 1, 1, 0, 1], [1, 1, 0, 0, 1]], [[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [1, 0, 0, 0, 0]],  [[0, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 1, 0, 0, 0]]]

def bestMeetingPoints(self, grids1):
    l = len(grids1)
    m = len(grids1[0])
    n = len(grids1[0][0])
    dim1Index = [i for i in range(l) for j in range(m) for k in range(n) if grids1[i][j][k] == 1]
    dim2Index = [j for i in range(l) for j in range(m) for k in range(n) if grids1[i][j][k] == 1]
    dim3Index = [k for i in range(l) for j in range(m) for k in range(n) if grids1[i][j][k] == 1]
    dim1Index.sort()
    dim2Index.sort()
    dim3Index.sort()
    dim1BMT = dim1Index[len(dim1Index) // 2]
    dim2BMT = dim2Index[len(dim2Index) // 2]
    dim3BMT = dim3Index[len(dim3Index) // 2]
    result = [dim1BMT, dim2BMT, dim3BMT]
    totalSumDistance = np.sum(np.abs(t - dim1BMT) for t in dim1Index) + 
    np.sum(np.abs(t - dim2BMT) for t in dim2Index) + 
    np.sum(np.abs(t - dim3BMT) for t in dim3Index)
    return totalSumDistance




def bestMeetingPoints(self, grids1):
    l = len(grids1)
    m = len(grids1[0])
    n = len(grids1[0][0])
    dim1Index = [i for i in range(l) for j in range(m) for k in range(n) if grids1[i][j][k] == 1]
    dim2Index = [j for i in range(l) for j in range(m) for k in range(n) if grids1[i][j][k] == 1]
    dim3Index = [k for i in range(l) for j in range(m) for k in range(n) if grids1[i][j][k] == 1]
    dim1Index.sort()
    dim2Index.sort()
    dim3Index.sort()
    dim1BMT = dim1Index[len(dim1Index) // 2]
    dim2BMT = dim2Index[len(dim2Index) // 2]
    dim3BMT = dim3Index[len(dim3Index) // 2]
    result = [dim1BMT, dim2BMT, dim3BMT]
    totalSumDistance = np.sum(np.abs(t - dim1BMT) for t in dim1Index) + 
    np.sum(np.abs(t - dim2BMT) for t in dim2Index) + np.sum(np.abs(t - dim3BMT) for t in dim3Index)
    return totalSumDistance, result



