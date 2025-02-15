class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        for s in strings:
            key = [0]
            if len(s) != 1:
                for i in range(len(s) - 1):
                    key.append((ord(s[i + 1]) - ord(s[i])) % 26)
                    print(s, key)
            result[tuple(key)].append(s)
        return [value for value in result.values()]