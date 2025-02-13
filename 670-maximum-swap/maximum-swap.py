class Solution:
    def maximumSwap(self, num: int) -> int:

        num_s = str(num)
        num_ls = list(num_s)

        max_digit_ind = len(num_s) - 1
        swap1, swap2 = -1, -1
        for j in range(len(num_ls) - 2, -1, -1):
            if num_ls[j] > num_ls[max_digit_ind]:
                max_digit_ind = j
            elif num_ls[j] < num_ls[max_digit_ind]:
                swap1 = j
                swap2 = max_digit_ind
            
        temp = num_ls[swap1]
        num_ls[swap1] = num_ls[swap2]
        num_ls[swap2] = temp
        return int(''.join(num_ls))