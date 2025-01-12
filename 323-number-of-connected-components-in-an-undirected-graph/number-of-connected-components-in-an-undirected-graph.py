class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i : [] for i in range(n)}
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        visited = set()
        def dfs(node):
            for nei in adj_list[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        count = 0
        for i in range(n):
            print(i)
            if i not in visited:
                visited.add(i)
                dfs(i)
                count += 1
        return count