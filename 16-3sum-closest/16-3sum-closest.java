class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int min = nums[0] + nums[1] + nums[nums.length - 1];
        for(int i = 0; i < nums.length; i++){
            int l = i+1;
            int r = nums.length - 1;
            while(l < r){
                int threeSum = nums[i] + nums[l] + nums[r];
                if (threeSum == target)
                    return threeSum;
                else if (threeSum > target)
                    r--;
                else
                    l++;
                
                if(Math.min(Math.abs(threeSum - target), Math.abs(target - threeSum)) < Math.min(Math.abs(min - target), Math.abs(target - min)))
                    min = threeSum;
            }
        }
        
        return min;
    }
}