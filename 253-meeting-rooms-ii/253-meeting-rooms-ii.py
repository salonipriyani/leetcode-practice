class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        s = 0
        e = 0
        rooms = count = 0
        while s < len(start):
            if start[s] < end[e]:
                s+=1
                count+=1
            else:
                e+=1
                count-=1
            rooms = max(rooms, count)
        return rooms
        