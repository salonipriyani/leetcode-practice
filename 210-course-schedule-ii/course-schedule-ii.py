class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_ls = {c : [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            adj_ls[crs].append(pre)
        
        visited = set()
        order = []
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            
            cycle.add(crs)
            for pre in adj_ls[crs]:
                if not dfs(pre):
                    return []
            visited.add(crs)
            cycle.remove(crs)
            order.append(crs)
            return True

        for i in range(numCourses):
            if i not in visited and dfs(i) == False:
                return []
        return order