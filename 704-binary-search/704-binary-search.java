class Solution {
    public int search(int[] nums, int target) {
        if (nums.length == 1)
            return target == nums[0] ? 0 : -1;
        int ans = -1;
        int start = 0, end = nums.length - 1;
        while (start <= end){
            int mid = (start + end)/2;
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] > target)
                end = mid - 1;
            else
                start = mid + 1;
        }
        
        return ans;
    }
}