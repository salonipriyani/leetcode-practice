class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
        sum_units = 0
        sum_boxes = 0
        for boxType in boxTypes:
            for i in range(boxType[0]):
                if sum_boxes + 1 <= truckSize:
                    sum_units += boxType[1]
                    sum_boxes += 1
                    
        return sum_units
                