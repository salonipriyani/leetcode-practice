class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        map = {}
        def recurse(amount):
            if amount == 0:
                return 0
            if amount in map:
                return map[amount]
            res = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + recurse(amount - coin))
            map[amount] = res
            return res
            

        res = recurse(amount)
        return -1 if res == float('inf') else res