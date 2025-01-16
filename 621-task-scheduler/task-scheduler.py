class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        for task in tasks:
            if task not in counter:
                counter[task] = 0
            counter[task] += 1
        
        arr = [-count for count in counter.values()]
        heapq.heapify(arr)
        q = deque()
        time = 0
        while arr or q:
            time += 1

            if arr:
                ct = 1 + heapq.heappop(arr)
                if ct:
                    q.append([ct, time + n])
            if q and q[0][1] == time:
                heapq.heappush(arr, q.popleft()[0])

        return time
                