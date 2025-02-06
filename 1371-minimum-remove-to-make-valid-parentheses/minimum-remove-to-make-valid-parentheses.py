class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        newstr = ""
        for i, letter in enumerate(s):
            if letter == '(' or letter == ')':
                if len(stack) == 0:
                    stack.append([i, letter])

                elif letter == ')' and stack[-1][1] == '(':
                    stack.pop()
                else:
                    stack.append([i, letter])
                
        print(stack)
        s_list = list(s)
        for i, letter in stack: 
            s_list[i] = ''
        new_s = ''.join(s_list)
        return new_s