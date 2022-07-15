class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Queue<List<Integer>> permutations = new LinkedList<>();
        permutations.offer(new ArrayList<>());
        for (int currNumber: nums){
            int size = permutations.size();
            for (int i = 0; i < size; i++){
                List<Integer> oldPermutation = permutations.poll();
                for (int j = 0; j <= oldPermutation.size(); j++){
                    List<Integer> newPermutation = new ArrayList<>(oldPermutation);
                    newPermutation.add(j, currNumber);
                    if (newPermutation.size() == nums.length)
                        res.add(newPermutation);
                    else
                        permutations.offer(newPermutation);
                }
            }
        }
        
        return res;
    }
}