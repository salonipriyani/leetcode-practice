class Solution {
    public int[] findRightInterval(int[][] intervals) {
        PriorityQueue<Integer> maxStartHeap = new PriorityQueue<>((i1, i2) -> intervals[i2][0] - intervals[i1][0]);
        PriorityQueue<Integer> maxEndHeap = new PriorityQueue<>((i1, i2) -> intervals[i2][1] - intervals[i1][1]);
        for (int i = 0; i < intervals.length; i++){
            maxStartHeap.offer(i);
            maxEndHeap.offer(i);
        }
        int[] result = new int[intervals.length];
        while (!maxEndHeap.isEmpty()){
            int topEnd = maxEndHeap.poll();
            result[topEnd] = -1;
            if(intervals[maxStartHeap.peek()][0] >= intervals[topEnd][1]){
                int topStart = maxStartHeap.poll();
                while (!maxStartHeap.isEmpty() && intervals[maxStartHeap.peek()][0] >= intervals[topEnd][1]){
                    topStart = maxStartHeap.poll();
                }
                
                result[topEnd] = topStart;
                maxStartHeap.add(topStart);
            }
            
        }
        
        return result;
    }
}