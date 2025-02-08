class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1
        
        topk = []
        for num, freq in freq_map.items():
            heapq.heappush(topk, [freq, num])
            if len(topk) > k:
                heapq.heappop(topk)
        topk_elements = []
        while topk:
            topk_elements.append(heapq.heappop(topk)[1])
        return topk_elements