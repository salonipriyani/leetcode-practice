class Solution {
    public int[] findErrorNums(int[] nums) {
        int[] ans = new int[2];
        int i = 0;
        while (i < nums.length){
            int j = nums[i] - 1;
            if (nums[i] != nums[j])
                swap(nums, i, j);
            else
                i++;
        }
        
        for (i = 0; i < nums.length; i++){
            if (nums[i] != i+1){
                ans[0] = nums[i];
                ans[1] = i + 1;
                break;
            }
        }
        
        return ans;
    }
    
    private void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}