class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        first_half = ""
        middle = ""
        count_map = {}

        for n in num:
            if n not in count_map:
                count_map[n] = 0
            count_map[n] += 1
        print(count_map)
        for i in range(9, -1, -1):
            print(i)
            if str(i) in count_map:
                digit = str(i)
                print(digit)
                digit_count = count_map[digit]
                num_pairs = digit_count // 2
                if num_pairs:
                    if len(first_half) == 0 and digit == "0":
                        count_map["0"] = 1
                    else:
                        for j in range(num_pairs):
                            first_half += digit
                if digit_count % 2 and len(middle) == 0:
                    middle = digit
        if not middle and not first_half:
            return "0"
        final_str = first_half + middle + first_half[::-1]
        return final_str     
                                                  





                                                      