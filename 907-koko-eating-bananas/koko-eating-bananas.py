class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l = 1
        r = max(piles)
        res = 1
        while l <= r:
            k = (l + r) // 2
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile/k)
            if time_taken <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res