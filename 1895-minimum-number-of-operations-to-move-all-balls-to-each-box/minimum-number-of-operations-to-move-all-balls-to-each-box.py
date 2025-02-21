class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        balls_to_left = moves_to_left = balls_to_right = moves_to_right = 0
        for i in range(n):
            res[i] += moves_to_left
            balls_to_left += int(boxes[i])
            moves_to_left += balls_to_left
            

            j = n - 1 - i
            res[j] += moves_to_right
            balls_to_right += int(boxes[j])
            moves_to_right += balls_to_right
            
        return res