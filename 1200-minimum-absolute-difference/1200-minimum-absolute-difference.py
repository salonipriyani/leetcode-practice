class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        
        left = 0
        res = []
        min_diff = float('inf')
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            min_diff = min(min_diff, diff)

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff == min_diff:
                res.append([arr[i-1], arr[i]])
                
        return res