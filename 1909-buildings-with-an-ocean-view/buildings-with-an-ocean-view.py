class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_ht = 0
        res = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_ht:
                res.append(i)
            max_ht = max(max_ht, heights[i])
        return res[::-1]