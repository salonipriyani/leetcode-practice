class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = {i : [] for i in range(1, n + 1)}    
        for src, tar, time in times:
            adj_list[src].append([time, tar])

        minHeap = [(0, k)]
        visited = set()
        res = 0

        while minHeap:
            dist, tar = heapq.heappop(minHeap)
            if tar in visited:
                continue
            visited.add(tar)
            res = dist

            for time2, nei in adj_list[tar]:
                if nei not in visited:
                    heapq.heappush(minHeap, [time2 + res, nei])
        
        return res if len(visited) == n else -1
