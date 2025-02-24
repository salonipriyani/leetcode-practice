class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = 0
        char_map = {}
        for c in tiles:
            if c not in char_map:
                char_map[c] = 0
            char_map[c] += 1
        
        def dfs():
            nonlocal res
            for c in char_map:
                if char_map[c] > 0:
                    res += 1
                    char_map[c] -= 1
                    dfs()
                    char_map[c] += 1
        


        dfs()
        return res