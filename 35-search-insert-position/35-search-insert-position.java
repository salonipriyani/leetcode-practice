class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left < right){
            if (nums[(left + right) / 2] == target)
                return (left + right)/2;
            else if (nums[(left + right) / 2] > target)
                right = (left + right)/2 - 1;
            else if (nums[(left + right) / 2] < target)
                left = (left + right)/2 + 1;
        }
        return nums[(left +  right)/2] < target ? (left + right)/2 + 1: (left + right)/2;
    }
}