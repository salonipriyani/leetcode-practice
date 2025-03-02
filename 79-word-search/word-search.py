class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        def recurse(i, j, word_idx):
            if word_idx == len(word):
                return True
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i, j) in path or board[i][j] != word[word_idx]:
                return False
            path.add((i, j))
            res = recurse(i + 1, j, word_idx + 1) or recurse(i - 1, j, word_idx + 1) or recurse(i, j + 1, word_idx + 1) or recurse(i, j - 1, word_idx + 1)
            path.remove((i, j))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if recurse(i, j, 0):
                    return True
        return False