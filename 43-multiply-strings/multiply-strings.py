class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" and num2 ==  "0":
            return "0"

        m = len(num1)
        n = len(num2) 
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                pos1 = i + j
                pos2 = i + j + 1
                total = mul + res[pos2]
                res[pos2] = total % 10
                res[pos1] += total // 10

        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        print(res)
        res_str_ls = [chr(num + ord('0')) for num in res[i:]]
        print(res_str_ls)
        res_str = ''.join(res_str_ls)
        return res_str if res_str else "0"