class Solution {
    public int findUnsortedSubarray(int[] nums) {
        boolean flag = false;
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for(int i = 1; i < nums.length; i++){
            if (nums[i] < nums[i-1])
                flag = true;
            if(flag)
                min = Math.min(min, nums[i]);
        }
        flag = false;
        for (int i = nums.length - 2; i >= 0; i--){
            if (nums[i] > nums[i+1])
                flag = true;
            if(flag)
                max = Math.max(max, nums[i]);
        }
        int start = 0, end = nums.length - 1;
        for (start = 0; start < nums.length; start++){
            if(min < nums[start]){
                break;
            }
        }
        
        for (end = nums.length - 1; end >= 0; end--){
            if(max > nums[end]){
                break;
            }
        }
        
        return end - start < 0 ? 0 : end - start + 1;
    }
}