class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i, val in enumerate(flowerbed):
            if val == 0:
                if len(flowerbed) == 1:
                    count += 1
                elif (i == 0 and flowerbed[i + 1] == 0) or (i == len(flowerbed) - 1 and flowerbed[i - 1] == 0 or (flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0)):
                    flowerbed[i] = 1
                    count += 1
        
        return True if count >= n else False