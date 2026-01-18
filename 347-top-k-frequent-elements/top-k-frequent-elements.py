class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0 
            count[num] += 1
        
        q = []
        for num, cnt in count.items():
            heapq.heappush(q, [cnt, num])
            if len(q) > k:
                heapq.heappop(q)
        res = []
        for i in range(k):
            res.append(heapq.heappop(q)[1])
        return res

