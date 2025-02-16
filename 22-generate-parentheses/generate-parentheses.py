class PStr:
    def __init__(self, openb, closeb, str):
        self.openb = openb
        self.closeb = closeb
        self.str = str

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q = deque()
        q.append(PStr(0, 0, ""))
        res= []
        while len(q) > 0:
            
            curr_pstr = q.popleft()
            print(curr_pstr.str)
            if curr_pstr.openb < n:
                q.append(PStr(curr_pstr.openb + 1, curr_pstr.closeb, curr_pstr.str + "("))
            if curr_pstr.closeb < curr_pstr.openb:
                q.append(PStr(curr_pstr.openb, curr_pstr.closeb + 1, curr_pstr.str + ")"))
            if curr_pstr.closeb == n:
                res.append(curr_pstr.str)
        return res
            