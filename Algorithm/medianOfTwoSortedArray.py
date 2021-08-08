#4. Median of Two Sorted Array:

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n_1 = len(nums1)
        n_2 = len(nums2)
        n = n_1 + n_2
        if n % 2 == 1:
            return self.kThSearch(nums1, nums2, n // 2)
        else:
            return ((self.kThSearch(nums1, nums2, n // 2)
            + ))

    def kThSearch(self, A, B, k):
        n_1 = len(A)
        n_2 = len(B)
        if not A:
            return B[k]
        if not B:
            return A[k]
        i_mA = len(A) // 2
        i_mB = len(B) // 2
        A_med = A[i_mA]
        B_med = B[i_mB]
        if k > (i_mA + i_mB):
            if A_med > B_med:
                return self.kThSearch(A, B[i_mB + 1:], k - i_mB - 1)
            else:
                return self.kThSearch(A[i_mA + 1:], B, k - i_mA - 1)
        else:
            if A_med > B_med:
                return self.kThSearch(A[:i_mA], B, k)
            else:
                return self.kThSearch(A, B[:i_mB], k)

#They use the activation function to add the non-linearity
#They use the bias here to incorporate the shifts
#

    def kThSearch(self, A, B, k):
        n_1 = len(A)
        n_2 = len(B)
        if not A:
            return B[k]
        if not B:
            return A[k]
        i_mA = len(A) // 2
        i_mB = len(B) // 2
        A_med = A[i_mA]
        B_med = B[i_mB]
        if k > (i_mA + i_mB):
            if A_med > B_med:
                return self.kThSearch(A, B[i_mB + 1:], k - i_mB - 1)
            else:
                return self.kThSearch(A[i_mA + 1: ], B, k - i_mA - 1)
        else:
            if A_med > B_med:
                return self.kThSearch(A[:i_mA], B, k)
            else:
                return self.kThSearch(A, B[: i_mB], k)




s1 = 2345
int(sum([int(t) ** 2 for t in str(s1)]))

def Kmeans(X):
    centroids = np.stack(self.initializeKmeansPlus(X), axis = 0)
    P = np.argmin(distance.cdist(X, centroids, 'euclidean'), axis = 1)
    for _ in range(self.maxIter):
        medianCentroids = np.vstack([np.median(X[P == i, :], axis = 1) for i in range(self.k)])
        tmp = np.argmin(distance.cdist(X, medianCentroids, 'euclidean'), axis = 1)
        if P == tmp:
            break
        P = tmp
    return P














