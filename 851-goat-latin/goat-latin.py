class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        for i in range(len(words)):
            word = words[i]
            if word[0] in "aeiouAEIOU":
                word = word + 'ma'
            else:
                l0 = word[0]
                word = word[1:]
                word += l0 + 'ma'
            word += 'a' * (i + 1)
            words[i] = word
        return ' '.join(words)
