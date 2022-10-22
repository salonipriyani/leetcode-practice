class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        def isBipartite(dislike_map, color, n, person_id):
            queue = []
            queue.append(person_id)
            color[person_id] = 1
            while queue:
                curr = queue.pop(0)
                for dislike in dislike_map[curr]:
                    if color[curr] == color[dislike]:
                        return False
                    if color[dislike] == -1:
                        color[dislike] = 1 - color[curr]
                        queue.append(dislike)
            return True
                    
        
        dislike_map = {}
        
        for curr in range(1, n+1):
            dislike_map[curr] = []
            
        for a, b in dislikes:
            dislike_map[a].append(b)
            dislike_map[b].append(a)
        colors = [-1] * (n+1)
        for person_id in range(1, n + 1):
            if colors[person_id] == -1:
                if not isBipartite(dislike_map, colors, n, person_id):
                    return False
        return True