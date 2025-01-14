class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf') for i in range(n)]
        prices[src] = 0
        for i in range(k + 1):
            tmpprices = prices.copy()
            for start, target, dist in flights:
                if prices[start] == float('inf'):
                    continue
                elif prices[start] + dist < tmpprices[target]:
                    tmpprices[target] = prices[start] + dist
            prices = tmpprices
        
        return -1 if tmpprices[dst] == float('inf') else tmpprices[dst]