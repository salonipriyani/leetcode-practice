class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        
        n = len(beginWord)
        intermediate_words = defaultdict(list)
        for word in wordList:
            for i in range(n):
                intermediate_words[word[:i] + "*" + word[i + 1:]].append(word)
        
        q = deque()
        q.append([beginWord, 1])
        visited = set()
        visited.add(beginWord)
        while q:
            word, dist = q.popleft()
            for i in range(n):
                intermediate = word[:i] + "*" + word[i + 1:]
                
                for intermediate_word in intermediate_words[intermediate]:
                    if intermediate_word == endWord:
                        return dist + 1
                    else:
                        if intermediate_word not in visited:
                            visited.add(intermediate_word)
                            q.append([intermediate_word, dist + 1])
        return 0
