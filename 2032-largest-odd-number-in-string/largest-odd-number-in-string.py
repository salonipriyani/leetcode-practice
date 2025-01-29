class Solution:
    def largestOddNumber(self, num: str) -> str:
        num_list = list(num)
        res_list = []
        for i in range(len(num_list) - 1, -1, -1):
            if int(num_list[i]) % 2:
                res_list = num_list[:i + 1]
                break
        
        return "".join(res_list)