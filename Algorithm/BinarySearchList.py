#BinarySearchList
def KthSearch(A, B, k):
    nA = len(A)
    nB = len(B)
    if not A:
        return B[k]
    if not B:
        return A[k]
    mA = nA//2
    mB = nB//2
    A_med = A[mA]
    B_med = B[mB]
    if k > (mA + mB):
        if A_med >= B_med:
            return KthSearch(A, B[mB+1 :], k - mB - 1)
        else:
            return KthSearch(A[mA+1:], B, k - mA - 1)
    else:
        if A_med >= B_med:
            return KthSearch(A[: mA], B, k)
        else:
            return KthSearch(A, B[:mB], k)

KthSearch([1, 2], [3, 4], 1)
KthSearch([1, 2], [3, 4], 2)
KthSearch([1, 2, 3], [5, 7, 9], 4)
KthSearch([1, 2], [3, 4], 2)
KthSearch([1, 2, 3, 4, 5], [6, 7], 4)


