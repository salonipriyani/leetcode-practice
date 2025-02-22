class Solution:
    def calculate(self, s: str) -> int:
        curr_num = 0
        stack = []
        sign = 1
       
        print(s)
        res = 0
        for i, char in enumerate(s):
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '+':
                res += sign * curr_num
                sign = 1
                curr_num = 0
            elif char == '-':
                res += sign * curr_num
                sign = -1
                curr_num = 0
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ')':
                res += sign * curr_num
                res *= stack.pop()
                res += stack.pop()
                curr_num = 0
        return res + sign * curr_num

        