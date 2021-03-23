#Divide_and_Conquer
def findMedianSortedArray(self, A, B):
    lengt = len(A) + len(B)
    if lengt % 2 == 1:
        return self.kThSearch(A, B, lengt // 2)
    else:
        return (self.kThSearch(A, B, lengt// 2) +
            self.kThSearch(A, B, lengt//2 - 1))

def kThSearch(self, A, B, k):
    if not A:
        return B[k]
    if not B:
        return A[k]
    i_mA = len(A) // 2
    i_mB = len(B) // 2
    mA = A[i_mA]
    mB = B[i_mB]
    if k > (i_mA + i_mB):
        if mA > mB:
            return self.kThSearch(A, B[i_mA + 1:], k - i_mB - 1)
        else:
            return self.kThSearch(A[i_mB + 1: ], B, k - i_mA - 1)
    else:
        if mA > mB:
            return self.kThSearch(A[:i_mA], B, k)
        else:
            return self.kThSearch(A, B[:i_mB], k)