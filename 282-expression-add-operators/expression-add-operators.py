class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []
        def recurse(index, prev_operand, curr_operand, value, string):
            if index == n:
                if value == target and curr_operand == 0:
                    res.append(''.join(string[1:]))
                return
            
            curr_operand = curr_operand * 10 + int(num[index])
            str_op = str(curr_operand)
            if curr_operand > 0:
                recurse(index + 1, prev_operand, curr_operand, value, string)
            
            string.append('+')
            string.append(str_op)
            recurse(index + 1, curr_operand, 0, value + curr_operand, string)
            string.pop()
            string.pop()

            if string:
                string.append('-')
                string.append(str_op)
                recurse(index + 1, -curr_operand, 0, value - curr_operand, string)
                string.pop()
                string.pop()

                string.append('*')
                string.append(str_op)
                recurse(index + 1, curr_operand * prev_operand, 0, value - prev_operand + (curr_operand * prev_operand), string)
                string.pop()
                string.pop()
        
        recurse(0, 0, 0, 0, [])
        return res