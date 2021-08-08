#249. Group Shifted Strings:
from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        strings.sort(key = lambda X: len(X))
        hashMaps = {}
        for s in strings:
        	keys = ()
            for i in range(len(s) - 1):
                curDif = (26 + ord(s[i + 1]) - ord(s[i])) % 26
                keys += curDif
            hashMaps[keys] = hashMaps.get(keys, []) + [s]
        return list(hashMaps.values())

hashMaps.get(keys, []) + [s]
#using a dictionary to store the history here.
#use the neighboring orders of the number in each char of the string
def groupStrings(self, strings):
    hashMaps = {}
    for s in strings:
        key = {}
        for i in range(len(s) - 1):
            curDif = ( 26 + ord(s[i + 1]) - ord(s[i])) % 26
            keys += (curDif, )
        hashMaps[keys] = hashMaps.get(keys, []).append([s])
    return list(hashMaps.values())

keys = ()
s = "ASDCSDCS"
for i in range(len(s) - 1):
    curDif = ( 26 + ord(s[i + 1]) - ord(s[i])) % 26
    keys += (curDif, )

hashMaps[keys] = hashMaps.get(keys, []) + [s]
hashMaps.get(keys, 0)


hashMaps[keys] = hashMaps.get(keys, []) + [s]



for i in range(len(s) - 1):
    curDif = (26 + ord(s[i + 1]) - ord(s[i])) % 26
    keys += (curDif, )
hashMaps[keys] = hashMaps.get(keys, []) + [s]
hashMaps.get(keys, 0)



def groupStrings(self, strings):
    hashMaps = {}
    for s in strings:
        keys = {}
        for i in range(len(s) - 1):
            curDif = (ord(s[i + 1]) - ord(s[i]) + 26) % 26
            keys += (curDif, )
        hashMaps[keys] = hashMaps.get(keys, []) + [s]
    return list(hashMaps.values())


def groupStrings(self, strings):
    hashMaps = {}
    for s in strings:
        keys = {}
        for i in range(len(s) - 1):
            curDif = (ord(s[i + 1]) - ord(s[i]) + 26) % 26
            keys += (curDif, )
        hashMaps[keys] = hashMaps.get(keys, []) + [s]
    return list(hashMaps.values())


def groupStrings(self, strings):
    hashMaps = {}
    for s in strings:
        keys = {}
        for i in range(len(s) - 1):
            curDif = (ord(s[i + 1]) - ord(s[i]) + 26) % 26
            keys += (curDif, )
        hashMap[keys] = hashMap.get(keys, []) + [s]
    result = list(hashMap.values())
    return result

def groupStrings(self, string):
    hashMaps = {}
    for s in strings:
        keys = {}
        for i in range(len(s) - 1):
            curDif = (ord(s[i + 1]) - ord(s[i]) + 26) % 26
            keys += (curDif, )
        hashMaps[keys] = hashMaps.get(keys, []) + [s]
    return list(hashMaps.values())

hashMaps[keys] = hashMaps.get(keys, []) + [s]

#store the index: [1, 1, num], [2, 3, num]
#store the index: [2, 3, num] ---> 

result = [[0 for in range(len(matrix2[0]))] for j in range(len(matrix1))]
for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j]:
            for k in range(len(B[0])):
                output[i][k] += A[i][j] * B[j][k]
return result

for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j]:
            for k in range(len(B[0])):
                output[i][k] += A[i][j] * B[j][k]
return result









