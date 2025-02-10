

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = {}

        for account in accounts:
            first_email = account[1]
            for i in range(2, len(account)):
                curr_email = account[i]
                if first_email not in adj_list:
                    adj_list[first_email] = []
                adj_list[first_email].append(curr_email)

                if curr_email not in adj_list:
                    adj_list[curr_email] = []
                adj_list[curr_email].append(first_email)
        
        res = []
        visited = set()

        def dfs(account, email):
            visited.add(email)
            account.append(email)
            
            if email not in adj_list:
                return
            for neighbor in adj_list[email]:
                if neighbor not in visited:
                    dfs(account, neighbor)

        for account in accounts:
            name = account[0]
            first_email = account[1]

            if first_email not in visited:
                merged_acc = []
                merged_acc.append(name)
                dfs(merged_acc, first_email)
                merged_acc[1:] = sorted(merged_acc[1:])
                res.append(merged_acc)
        return res


