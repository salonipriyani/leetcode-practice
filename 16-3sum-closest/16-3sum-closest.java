class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int min = nums[0] + nums[1] + nums[nums.length - 1];
        int l, r, threeSum;
        for(int i = 0; i < nums.length; i++){
            l = i+1;
            r = nums.length - 1;
            while(l < r){
                threeSum = nums[i] + nums[l] + nums[r];
                if (threeSum == target)
                    return threeSum;
                else if (threeSum > target)
                    r--;
                else
                    l++;
                
                if(Math.abs(threeSum - target) < Math.abs(min - target))
                    min = threeSum;
            }
        }
        
        return min;
    }
}