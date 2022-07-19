class MedianFinder {
    PriorityQueue<Integer> maxHeap;
    PriorityQueue<Integer> minHeap;
    
    public MedianFinder() {
        maxHeap = new PriorityQueue<>((a,b) -> b-a);
        minHeap = new PriorityQueue<>((a,b) -> a-b);
    }
    
    public void addNum(int num) {
        if (maxHeap.isEmpty() || maxHeap.peek() >= num)
            maxHeap.add(num);
        else
            minHeap.add(num);
        
        if (maxHeap.size() > minHeap.size() + 1)
            minHeap.add(maxHeap.poll());
        else if (maxHeap.size() < minHeap.size())
            maxHeap.add(minHeap.poll());
    }
    
    public double findMedian() {
        if (minHeap.size() == maxHeap.size())
            return (minHeap.peek() / 2.0 + maxHeap.peek()/2.0);
        return maxHeap.peek();
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */