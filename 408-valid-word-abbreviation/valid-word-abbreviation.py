class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(abbr) > len(word):
            return False
        
        j = 0
        i = 0
        while i < len(abbr):
            letter = abbr[i]
            if letter.isdigit():
                if letter == '0':
                    return False
                curr_num = 0
                while i < len(abbr) and abbr[i].isdigit():
                    curr_num = (curr_num * 10) + int(abbr[i])
                    i += 1
                j += curr_num
                
            else:
                if j >= len(word) or abbr[i] != word[j]:
                    return False
                j += 1
                i += 1
        return True if j == len(word) and i == len(abbr) else False