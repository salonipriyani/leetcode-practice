class Solution {
    
    private Map<String, Integer> map = new HashMap<>();
    public int findTargetSumWays(int[] nums, int target) {
        return backtrack(nums, target, 0, 0);
    }
    
    public int backtrack(int[] nums, int target, int index, int total){
        if (index == nums.length){
            if (total == target)
                return 1;
            else
                return 0;
        }
        String s = index + "()" + total;
        if (map.containsKey(s))
            return map.get(s);
        map.put(s, backtrack(nums, target, index+1, total + nums[index]) + backtrack(nums, target, index+1, total - nums[index]));
        
        return map.get(s);
            
    }
}