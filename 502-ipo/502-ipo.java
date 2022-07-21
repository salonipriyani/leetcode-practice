class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        PriorityQueue<Integer> maxProfitHeap = new PriorityQueue<>((i1, i2) -> profits[i2] - profits[i1]);
        PriorityQueue<Integer> minCapitalHeap = new PriorityQueue<>((i1, i2) -> capital[i1] - capital[i2]);
        
        int availableCapital = w;
        for (int i = 0; i < capital.length; i++)
            minCapitalHeap.offer(i);
        
        for (int i = 0; i < k; i++){
            while (!minCapitalHeap.isEmpty() && capital[minCapitalHeap.peek()] <= availableCapital)
                maxProfitHeap.offer(minCapitalHeap.poll());
            
            if (maxProfitHeap.isEmpty())
                break;
            
            availableCapital += profits[maxProfitHeap.poll()];
        }
        
        return availableCapital;
    }
}