class Solution {
    public int maxSubArray(int[] nums) {
        int maxSoFar = Integer.MIN_VALUE;
        int maxTillHere = 0;
        for (int i = 0; i < nums.length; i++){
            maxTillHere += nums[i];
            if(maxSoFar < maxTillHere)
                maxSoFar = maxTillHere;
            if(maxTillHere < 0)
                maxTillHere = 0;
        }
        return maxSoFar;
    }
}