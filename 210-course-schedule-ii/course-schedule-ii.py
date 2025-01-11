class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c : [] for c in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)
        # output = final list
        # visited = that have been visited
        # cycle = within this cycle
        output = []
        visited, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in adj[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return output
