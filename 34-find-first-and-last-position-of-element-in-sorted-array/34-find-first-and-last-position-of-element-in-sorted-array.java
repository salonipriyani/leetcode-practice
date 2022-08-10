class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] ans = new int[]{-1, -1};
        ans[0] = findNumber(nums, false, target);
        if (ans[0] != -1)
            ans[1] = findNumber(nums, true, target);
        return ans;
    }
    
    public int findNumber(int[] nums, boolean maxIndexSearch, int target){
        int start = 0, end = nums.length - 1;
        int index = -1;
        while (start <= end){
            int mid = (start + end)/2;
            if (nums[mid] > target)
                end = mid - 1;
            else if (nums[mid] < target)
                start = mid + 1;
            else{ // nums[i] == target
                index = mid;
                if (maxIndexSearch)
                    start = mid + 1;
                else
                    end = mid - 1;
            }
        }
        return index;
    }
}