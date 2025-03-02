class Solution:
    def jump(self, nums: List[int]) -> int:
        q = deque()
        q.append(0)
        visited = set()
        visited.add(0)
        parent = {0: None}
        res = []
        while q:
            flag = 0
            curr = q.popleft()
            for i in range(curr + 1, min(len(nums), curr + nums[curr] + 1)):
                if i not in visited:
                    visited.add(i)
                    parent[i] = curr
                    q.append(i)
                    if i == len(nums) - 1:
                        while i != None:
                            res.append(i)
                            i = parent[i]
                        flag = 1
                        break
            if flag == 1:
                break
        print(res[::-1])
        return len(res) - 1 if len(res) > 0 else 0