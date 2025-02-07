class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1_cp = nums1[:m]

        p1 = 0
        p2 = 0

        while p1 < m and p2 < n:
            if nums1_cp[p1] < nums2[p2]:
                nums1[p1 + p2] = nums1_cp[p1]
                p1 += 1
            elif nums1_cp[p1] >= nums2[p2]:
                nums1[p1+p2] = nums2[p2]
                p2 += 1
            
        if p1 < m:
            nums1[p1 + p2 : m + n] = nums1_cp[p1:]
        if p2 < n:
            nums1[p1 + p2 : m + n] = nums2[p2:]
        
