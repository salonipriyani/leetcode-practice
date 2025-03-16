class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # 0, 1, 8 -> same
        # 6 -> 9
        # 9 -> 6
        rotated_str = []
        for i in range(len(num) - 1, -1, -1):
            c = num[i]
            if c in ('0', '1', '8'):
                rotated_str.append(c)
            elif c == '6':
                rotated_str.append('9')
            elif c == '9':
                rotated_str.append('6')
            else:
                return False
        rotated = ''.join(rotated_str)
        return rotated == num