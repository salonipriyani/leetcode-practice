class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {i : [] for i in range(n)}

        for node, nei in edges:
            adj_list[node].append(nei)
            adj_list[nei].append(node)

        visited = set()
        q = deque()
        q.append((0, -1))
        visited.add(0)

        while q:
            node, parent = q.popleft()
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                visited.add(nei)
                q.append((nei, node))
        return len(visited) == n