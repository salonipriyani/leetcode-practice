class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> nums = new ArrayList<>();
        
        for (int i = 0; i <= rowIndex; i++){
            nums.add(1);
            for (int j = i - 1; j >= 1; j--){
                nums.set(j, nums.get(j) + nums.get(j-1));
            }
        }
        
        return nums;
    }
}