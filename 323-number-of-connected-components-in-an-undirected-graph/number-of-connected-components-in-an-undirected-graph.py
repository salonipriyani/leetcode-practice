class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i : [] for i in range(n)}
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        visited = set()
        
        def bfs(node):
            q = deque()
            q.append(node)
            visited.add(node)
            while q:
                curr = q.popleft()
                for nei in adj_list[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)


        count = 0
        for i in range(n):
            print(i)
            if i not in visited:
                visited.add(i)
                bfs(i)
                count += 1
        return count