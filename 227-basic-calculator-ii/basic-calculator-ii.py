class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = []
        curr_num = 0
        operation = '+'
        for i, char in enumerate(s):
            if char == ' ':
                continue
            if char.isdigit():
                curr_num = (curr_num * 10) + int(char)
            if char in ('+', '-', '/', '*') or i == len(s) - 1:
                if operation == '-':
                    stack.append(-curr_num)
                elif operation == '+':
                    stack.append(curr_num)
                elif operation == "*":
                    stack.append(stack.pop() * curr_num)
                elif operation == '/':
                    top = stack.pop()
                    if top < 0:
                        to_add = -(-top // curr_num)
                    else:
                        to_add = top // curr_num
                    stack.append(to_add)
                operation = char
                curr_num = 0
        return sum(stack)
