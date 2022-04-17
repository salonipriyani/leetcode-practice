class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> totalSet = new HashSet<>();
        Arrays.sort(nums);
        int j, k;
        for ( int i = 0; i < nums.length - 2; i++){
            j = i + 1;
            k = nums.length - 1;
            while(j < k){
                if(nums[i] + nums[j] + nums[k] > 0)
                    k--;
                else if(nums[i] + nums[j] + nums[k] < 0)
                    j++;
                else{
                    totalSet.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++;
                    k--;
                }
            }
        }
        return new ArrayList<>(totalSet);
    }
}