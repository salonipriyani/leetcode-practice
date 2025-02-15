class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1:
            return True

        pre_map = {}
        for course, pre in prerequisites:
            if course not in pre_map:
                pre_map[course] = []
            pre_map[course].append(pre)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if course not in pre_map:
                return True

            visited.add(course)
            for pre in pre_map[course]:
                if dfs(pre) == False:
                    return False
            pre_map[crs] = []
            visited.remove(course)
            return True

        for crs, pre in pre_map.items():
            if dfs(crs) == False:
                return False
        return True   