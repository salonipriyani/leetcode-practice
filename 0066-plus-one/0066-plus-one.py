class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = "".join([str(digit) for digit in digits])
        num = int(num_str)
        num += 1
        num_new_str = str(num)
        ls = list(num_new_str)
        
        for i in range(len(ls)):
            ls[i] = int(ls[i])
            
        return ls
        