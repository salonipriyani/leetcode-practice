class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        ans.add(new ArrayList<>());
        for (int currNumber: nums){
            int size = ans.size();
            for (int i = 0; i < size; i++){
                List<Integer> set = new ArrayList<>(ans.get(i));
                set.add(currNumber);
                ans.add(set);
            }
        }
        
        return ans;
    }
}