class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minheap = []

        for i in range(k):
            x = points[i][0]
            y = points[i][1]
            dist = -(x*x + y*y)
            heapq.heappush(minheap, [dist, points[i]])
        
        for i in range(k, len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            dist1 = (x1 * x1) + (y1 * y1)
            dist2 = - minheap[0][0]
            if dist1 < dist2:
                heapq.heappop(minheap)
                heapq.heappush(minheap, [-dist1, points[i]])
        res = []
        for dist, points in minheap:
            res.append(points)
        
        return res
