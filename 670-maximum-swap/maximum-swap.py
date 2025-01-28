class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        max_digit_ind = len(num_list) - 1
        swap1 = -1
        swap2 = -1
        for j in range(len(num_list) - 2, -1, -1):
            if num_list[j] > num_list[max_digit_ind]:
                max_digit_ind = j
            elif num_list[j] < num_list[max_digit_ind]:
                swap1 = j
                swap2 = max_digit_ind
        
        temp = num_list[swap1]
        num_list[swap1] = num_list[swap2]
        num_list[swap2] = temp

        new_num = int("".join(num_list))
        return new_num