class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        def quickselect(arr, k):
            pivot = arr[0]
            left, right, mid = [], [], []

            for num in arr:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            
            if k <= len(left):
                return quickselect(left, k)
            
            if k > len(left) + len(mid):
                return quickselect(right, k - len(left) - len(mid))
            return pivot
        return quickselect(nums, k)

                    
