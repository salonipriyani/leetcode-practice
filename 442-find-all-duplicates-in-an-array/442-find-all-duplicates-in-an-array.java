class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        int i = 0;
        while (i < nums.length){
            int j = nums[i] - 1;
            if (nums[i] != nums[j])
                swap(nums, i, j);
            else
                i++;
        }
        List<Integer> ans = new ArrayList<>();
        for (i = 0; i < nums.length; i++){
            if(nums[i] != i+1)
                ans.add(nums[i]);
        }
        
        return ans;
    }
    
    private void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}