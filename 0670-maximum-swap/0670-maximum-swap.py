class Solution:
    def maximumSwap(self, num: int) -> int:
        num_arr = list(str(num))
        
        for i in range(len(num_arr) - 1):
            if num_arr[i] < num_arr[i + 1]:
                break
        else:
            return num
        max_num = num_arr[i]
        max_idx = i
        for j in range(i + 1, len(num_arr)):
            if num_arr[j] >= max_num:
                max_num = num_arr[j]
                max_idx = j
        min_num = num_arr[i]
        min_idx = i
        for j in range(i - 1, -1, -1):
            if num_arr[j] < max_num:
                min_idx = j
                
        num_arr[min_idx], num_arr[max_idx] = num_arr[max_idx], num_arr[min_idx]
        
        return int(''.join(num_arr))
                
            