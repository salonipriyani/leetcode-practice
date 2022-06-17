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
        int count = 0;
        count += backtrack(nums, target, index+1, total + nums[index]);
        count += backtrack(nums, target, index+1, total - nums[index]);
        map.put(s, count);
        
        return map.get(s);
            
    }
}