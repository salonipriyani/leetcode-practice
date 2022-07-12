class Solution {
    public int missingNumber(int[] nums) {
        int i = 0;
        
        while (i < nums.length){
            if (nums[i] < nums.length && nums[i] != nums[nums[i]])
                swap(nums, i, nums[i]);
            else
                i++;
        }
        
        for (i = 0; i < nums.length; i++){
            if (i != nums[i])
                return i;
        }
        
        return nums.length;
    }
    
    public void swap (int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    
}