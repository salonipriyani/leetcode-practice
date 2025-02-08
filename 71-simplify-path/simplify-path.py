class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        i = 0
        while i < len(path):
            print("i", i)
            dir_name = ""
            if path[i] == '/':
                while i < len(path) and path[i] == '/':
                    i += 1
            elif path[i] == '.':
                len_period = 0
                j = i
                while j < len(path) and (path[j] != '/'):
                    len_period += 1
                    j += 1
                if len_period == 1:
                    i += 1
                elif len_period == 2 and path[i : i + 2] == '..':
                    if len(stack) > 0:
                        stack.pop()
                    i += 2
                else:
                    stack.append(path[i : i + len_period])
                    i += len_period
                    # i += len_period
                    # while i < len(path) and path[i].isalpha():
                    #     dir_name += path[i]
                    #     i += 1
                    # stack.append(dir_name)
            else:
                while i < len(path) and path[i] != '/':
                    dir_name += path[i]
                    i += 1
                print("dir_name", dir_name)
                stack.append(dir_name)

                
        res = ""
        if len(stack) == 0:
            return "/"
        else:
            for ele in stack:
                res += f"/{ele}"
        return res
