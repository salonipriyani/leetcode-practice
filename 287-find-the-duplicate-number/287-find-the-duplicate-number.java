class Solution {
    public int findDuplicate(int[] nums) {
        int low = 0, high = nums.length - 1;
        int duplicate = -1;
        while (low <= high){
            int mid = (low + high)/2;
            int count = 0;
            for (int num: nums){
                if (num <= mid)
                    count++;
            }
            
            if(count > mid){
                high = mid - 1;
                duplicate = mid;
            }
            else
                low = mid + 1;
        }
        
        return duplicate;
    }
}