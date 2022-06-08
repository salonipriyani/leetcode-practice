class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> ans = new ArrayList<>();
        for(int[] interval: intervals){
            if (newInterval[1] < interval[0]){
                ans.add(newInterval);
                newInterval = interval;
            }
            else if (newInterval[0] > interval[1]){
                ans.add(interval);
            }
            else{
                int min = Math.min(interval[0], newInterval[0]);
                int max = Math.max(interval[1], newInterval[1]);
                newInterval = new int[]{min, max};
            }
        }
        ans.add(newInterval);
        
        return ans.toArray(new int[ans.size()][]);
    }
}