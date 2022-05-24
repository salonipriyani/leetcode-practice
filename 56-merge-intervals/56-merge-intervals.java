class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> (a[0] - b[0]));
        List<int []> ans = new ArrayList<>();
        ans.add(intervals[0]);
        int ansSize = 1;
        for (int i = 1; i < intervals.length; i++){
            int s = intervals[i][0];
            int e = intervals[i][1];
            if(ans.get(ansSize - 1)[1] >= intervals[i][0]){
                ans.get(ansSize - 1)[1] = Math.max(ans.get(ansSize-1)[1], intervals[i][1]);
            }
            else{
                ans.add(intervals[i]);
                ansSize++;
            }
        }
        
        return ans.toArray(new int[0][]);
    }
}