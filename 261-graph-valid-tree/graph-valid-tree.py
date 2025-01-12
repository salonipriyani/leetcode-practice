class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {i : [] for i in range(n)}

        for node, nei in edges:
            adj_list[node].append(nei)
            adj_list[nei].append(node)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                else:
                    if dfs(nei, node) == False:
                        return False
            return True
        
        return dfs(0, -1) and len(visited) == n