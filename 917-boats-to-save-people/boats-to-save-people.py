class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0
        r = len(people) - 1
        n_boats = 0
        while l <= r:
            if l != r:
                if people[l] + people[r] <= limit:
                    n_boats += 1
                    l += 1
                    r -= 1
                else:
                    n_boats += 1
                    r -= 1

            else:
                n_boats += 1
                l += 1
                r -= 1

        
        return n_boats
