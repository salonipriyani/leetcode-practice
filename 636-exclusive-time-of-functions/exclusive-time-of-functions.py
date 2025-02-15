class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        s = logs[0].split(':')
        function_id, start, end = s[0], s[1], s[2]
        stack.append(int(function_id))
        res = [0] * n
        i = 1
        time = int(end)
        prev = int(end)
        while i < len(logs):
            ls = logs[i].split(':')
            print(ls)
            function_id, startorend, timestamp = int(ls[0]), ls[1], int(ls[2])
            if startorend == 'start':
                if len(stack) != 0:
                    res[stack[-1]] += timestamp - prev
                stack.append(function_id)
                prev = timestamp
            else:
                res[stack[-1]] += timestamp - prev + 1
                stack.pop()
                prev = timestamp + 1
            i += 1
        return res