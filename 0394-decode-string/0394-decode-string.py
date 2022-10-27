class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        for i, c in enumerate(s):
            if c == ']':
                decoded_string = []
                while len(stack)!=0 and stack[len(stack) - 1] != '[':
                    decoded_string.append(stack.pop())
                stack.pop()
                base = 1
                k = 0
                while len(stack) != 0 and stack[-1].isdigit():
                    k = k + (int(stack.pop()) * base)
                    base = base * 10
                #n = int(stack.pop())
                for i in range(k):
                    for j in range(len(decoded_string) -1, -1, -1):
                        stack.append(decoded_string[j])
            else:
                stack.append(c)
        res = [0] * len(stack)
        
        for i in range(len(res)-1, -1, -1):
            res[i] = stack.pop()
            
        return "".join(res)
            