class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0, sum = 0, ans = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++){
            sum += nums[i];
            while (sum >= target){
                ans = Math.min(ans, i+1-left);
                sum -= nums[left];
                left++;
            }
        }
        return ans != Integer.MAX_VALUE ? ans : 0;
    }
}