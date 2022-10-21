class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        
        for a in set(words[0]):
            count = words[0].count(a)
            occurances = 1
            for i in range(1, len(words)):
                if a in words[i]:
                    count = min(count, words[i].count(a))
                    occurances += 1
                else:
                    break
            
            if occurances == len(words):
                for i in range(count):
                    res.append(str(a))
        
        return res
                