class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = {}
        for char in s:
            if char not in freq_map:
                freq_map[char] = 0
            freq_map[char] += 1

        maxheap = []
        for char, count in freq_map.items():
            maxheap.append([-count, char])
        heapq.heapify(maxheap)
        res = ""
        while maxheap:
            count, char = heapq.heappop(maxheap)
            if not res or res[-1] != char:
                res += char
                if count + 1 < 0:
                    heapq.heappush(maxheap, [count + 1, char])
            else:
                if not maxheap:
                    return ''
                second_count, second_char = heapq.heappop(maxheap)
                res += second_char
                if second_count + 1 < 0:
                    heapq.heappush(maxheap, [second_count + 1, second_char])
                heapq.heappush(maxheap, [count, char])
        return res                
