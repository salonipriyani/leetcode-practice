class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]
        n = len(intervals)
        starts.sort()
        ends.sort()
        i = 0
        j = 0
        num = 0
        max_num = 0
        while i < n:
            if starts[i] < ends[j]:
                num += 1
                if num > max_num:
                    max_num = num
                i += 1
            else:
                num -= 1
                j += 1
        return max_num
