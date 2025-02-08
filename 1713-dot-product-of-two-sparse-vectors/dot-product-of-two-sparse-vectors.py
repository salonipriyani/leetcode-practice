class SparseVector:
    def __init__(self, nums: List[int]):
        self.map = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.map[i] = num


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        #self.map
        #vec.map
        dot_prod = 0
        for i in self.map.keys():
            if i in vec.map:
                dot_prod += (self.map[i] * vec.map[i])
        return dot_prod
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)