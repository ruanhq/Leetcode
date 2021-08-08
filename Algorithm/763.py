#partition labels:
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        sortedLast = sorted(last.items(), key = lambda X: X[1])
        start = end = 0
        result = []
        for i, c in enumerate(S):
            end = max(end, last[c])
            if i == end:
                output.append(end - start + 1)
                start = i + 1
        return output


sortedLast = sorted(last.items(), key=lambda kv: kv[1])
sortedX = sorted(last.items(), key = lambda kv: kv[1])

#partition labels: sort by the values and then rank them together



