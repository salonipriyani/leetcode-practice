class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        int count = 0;
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
        
        int[] previous = intervals[0];
        for (int i = 1; i < intervals.length; i++){
            int[] current = intervals[i];
            
            if (previous[1] > current[0]){
                count++;
                continue;
            }
                
            
            previous = current;
        }
        
        return count;
    }
}