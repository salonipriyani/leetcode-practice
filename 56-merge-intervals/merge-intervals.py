class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        res.append([intervals[0][0], intervals[0][1]])
        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            if curr_start <= res[len(res) - 1][1]:
                res[len(res) - 1][1] = max(res[len(res) - 1][1], curr_end)
                res[len(res) - 1][0] = min(res[len(res) - 1][0], curr_start)
            else:
                res.append([curr_start, curr_end])
        
        return res