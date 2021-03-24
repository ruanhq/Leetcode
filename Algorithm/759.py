#759. Employee Free Time:
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervalList = []
        for i in schedule:
            [intervalList.append(x) for x in i]
        intervalList.sort(key = lambda X: X.start)
        mergedInterval = []
        for interval in intervalList:
            if not mergedInterval or interval.start > mergedInterval[-1].end:
                mergedInterval.append(interval)
            else:
                mergedInterval[-1].end = max(interval.end, mergedInterval[-1].end)
        freeList = []
        for i in range(1, len(mergedInterval)):
            freeList.append(Interval(start = mergedInterval[i - 1].end, end = mergedInterval[i].start))
        return freeList

