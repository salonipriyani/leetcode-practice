class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_ls = defaultdict(set)
        in_degree = {c : 0 for word in words for c in word}

        for first_word, second_word in zip(words, words[1:]):
            flag = 0
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_ls[c]:
                        adj_ls[c].add(d)
                        in_degree[d] += 1
                    flag = 1
                    break
            if flag == 0:
                if len(second_word) < len(first_word):
                    return ""
        output = []
        q = deque()
        for c in in_degree:
            if in_degree[c] == 0:
                q.append(c)

        while q:
            c = q.popleft()
            output.append(c)
            for next_char in adj_ls[c]:
                in_degree[next_char] -= 1
                if in_degree[next_char] == 0:
                    q.append(next_char)
        
        if len(output) != len(in_degree):
            return ""

        return ''.join(output)

