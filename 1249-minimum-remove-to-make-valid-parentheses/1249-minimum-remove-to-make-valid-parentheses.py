class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_to_remove = set()
        index_stack = []
        
        for i, c in enumerate(s):
            if c not in "()":
                continue
            
            if c == '(':

                index_stack.append(i)
            elif c == ')':
                if len(index_stack) == 0:
                    index_to_remove.add(i)
                else:
                    index_stack.pop()
            
        
        index_to_remove = index_to_remove.union(set(index_stack))
        
        string_builder = []

        for i,c in enumerate(s):
            if i not in index_to_remove:
                string_builder.append(c)
                
        return "".join(string_builder)
            
            