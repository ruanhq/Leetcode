#get the k smallest ones:

import heapq

sss1 = [[1, 3], [2, 0.5], [3, 0.5], [4, 7], [-3, 6],
[1, 25], [3, 0.6]]
heap = []
for point in sss1:
    dist = point[0] ** 2 + point[1] ** 2
    heapq.heappush(heap, (-dist, point))
    if len(heap) > 3:
        heapq.heappop(heap)

for point in sss1:
    dist = point[0] ** 2 + point[1] ** 2
    heapq.heappush(heap, (-dist, point))
    #Find the first k element here:
    if len(heap) > 3:
        heapq.heappop(heap)


#pop out the largest element
#heappush into the (-dist, point)
for point in sss1:
    dist = point[0] ** 2 + point[1] ** 2
    heapq.heappush(heap, (-dist, point))
    if len(heap) > 3:
        heapq.heappop(heap)


heapq.heappush(heap, (-dist, point))

#heapify:
import heapq
from heapq import heapify, heappop
heap0 = [9, 3, 1, 5, 6, 2, 7]
heap_neg = [-x for x in heap0]
heapify(heap_neg)#ascending, pop the largest element.
heap1 = [(-9, 9), (-3, 3), (-1, 1), (-5, 5), (-6, 6), (-2,2), (-7,7)]
heap2 = []
for pts in heap1:
    distance = pts[0] ** 2 + pts[1] ** 2
    heapq.heappush(heap2, (-distance, pts))
#looks like the deque:
heapify(heap2, key = lambda X: -X)
#_heapify_max makes the 
from heapq import heapify, heappop, _heapify_max
heap3 = [9, 3, 1, 5, 6, 2, 7]
_heapify_max(heap3)


heap = []
for point in points:
    dist = point[0] * point[0] + point[1] * point[1]
    heapq.heappush(heap, (-dist, point))
    if len(heap) > k:
        heapq.heappop(heap)

heap = []
for point in points:
    dist = point[0] ** 2 + point[1] ** 2
    heapq.heappush(heap, (-dist, point))
_heapify_max(heap3)
_heapify_max(heap3)

heappop(heap3)
heappop(heap3)
_heapify_max(heap3)

heappop(heap3)
_heapify_max(heap3)

class Solution(object):
    def reorganizeString(self, S):
        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (N + 1) / 2:
                return ""
            A.extend(c * x)
        if N % 2 == 0:






#pandas implement window function:
df = pd.DataFrame({'key1': ['a', 'a', 'a', 'b', 'a'],
'data1': [1, 2, 2, 3, 3],
'data2': [1, 10, 2, 3, 30]})

#get the window function:
df['RN1'] = df.groupby('key1')['data1'].rank(method = 'min')
df['RN2'] = df.groupby('key1')['data2'].rank(ascending = False) - 1
df['RN3'] = df.sort_values(['data1', 'data2'], ascending = [True, False]).groupby(['key1']).cumcount()

df['RN5'] = df.groupby(['key1'])['data1'].rank(method = 'max')
df['RN6'] = df.groupby('key1')['data1'].transform(lambda X: X.rank(method = 'dense', ascending = False))
df['RN7'] = df.groupby('key1')['data2'].transform(lambda X: X.rank(method = 'dense'))

df['RK'] = df.groupby('key1', sort = True).ngroup() + 1


df['RN8'] = df.groupby('key1')['data3'].transform(lambda X: X.rank(method = 'dense'))

df["RN9"] = df.groupby('key1')['data1'].apply(lambda X: X.rank(method = 'dense'))

df["RN10"] = df.groupby("key1")['data1'].rank("dense", ascending = True)

df["RN11"] = df.groupby('key1')['data1'].rank('dense', ascending = False)
df["RN12"] = df.groupby('key2')['data1'].rank('dense', ascending = True)
result = [1,2, 3]
result.extend([4, 5, 6])
result

#find the k largest one:
(SELECT col1, COUNT(DISTINCT col2) AS col3
FROM TB
GROUP BY col1 
ORDER BY col1)
LIMIT 1;

(SELECT A1, COUNT(DISTINCT col2) AS col3
FROM Table
GROUP BY col1
ORDER BY col1)
LIMIT 1;





