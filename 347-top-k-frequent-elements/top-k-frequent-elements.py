class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1
        
        minheap = []
        for num, freq in freq_map.items():
            heapq.heappush(minheap, [freq, num])

            if len(minheap) > k:
                heapq.heappop(minheap)

        return [item[1] for item in minheap]