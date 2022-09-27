class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: int(x[0]))
        res = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                res.append(prev)
                prev = curr
        
        res.append(prev)
        return res
        
        
            