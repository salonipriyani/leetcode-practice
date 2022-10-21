class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_arr = []
        for i in range(len(arr)):
            if i == 0:
                missing = arr[i] - 0 - 1
                for i in range(1, arr[i]):
                    missing_arr.append(i)
            else:
                missing = arr[i] - arr[i-1] - 1
                for i in range(arr[i-1] +1, arr[i]):
                    missing_arr.append(i)
            if len(missing_arr) >= k:
                print(missing_arr)
                return missing_arr[k-1]
       
        
        a = arr[-1] + 1
        while True:
            missing_arr.append(a)
            a += 1
            if len(missing_arr) >= k:
                print(missing_arr)
                return missing_arr[k-1]
        
            