class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] ans = new int[nums.length - k + 1];
        Deque<Integer> dq = new LinkedList<>();
        int left = 0;
        for (int right = 0; right < nums.length; right++){
            while (!dq.isEmpty() && nums[right] >= nums[dq.getLast()])
                dq.removeLast();
            dq.addLast(right);
            
            if(left > dq.getFirst())
                dq.removeFirst();
            if(right + 1 >= k){
                ans[left] = nums[dq.getFirst()];
                left++;
            }    
        }
        return ans;
        
    }
}