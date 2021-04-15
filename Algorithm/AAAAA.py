class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        c, s = collections.Counter(features), set(features)
        for response in responses:
            currentWords = set(response.split(' '))
            for word in currentWords:
                if word in s:
                    c[word] += 1
        freqDict = sorted(c.items(), key = lambda X: -X[1])
        return [p[0] for p in freqDict]

#dict: items()
#Counter().items()
#

#meeting rooms II:

class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        c, s = collections.Counter(features), set(features)
        for response in responses:
            currentWords = set(response.split(" "))
            for word in currentWords:
                if word in s:
                    c[word] += 1
        freqDict = sorted(c.items(), key = lambda X: -X[1])
        return [p[0] for p in freqDict]
        