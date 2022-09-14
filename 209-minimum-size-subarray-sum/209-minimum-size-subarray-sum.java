class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        
        int windowStart = 0, currSum = 0, minLength = Integer.MAX_VALUE;
        for (int windowEnd = 0; windowEnd < nums.length; windowEnd++){
            currSum += nums[windowEnd];
            while (currSum >= target){
                minLength = Math.min(minLength, windowEnd - windowStart + 1);
                currSum -= nums[windowStart];
                windowStart++;
            }
        }
        return minLength != Integer.MAX_VALUE? minLength : 0;
    }
}