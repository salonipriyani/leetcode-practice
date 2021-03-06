class MyCircularQueue {
    
    int maxSize, front = 0, rear = -1;
    int[] data;

    public MyCircularQueue(int k) {
        data = new int[k];
        maxSize = k;
    }
    
    public boolean enQueue(int value) {
        if(isFull())
            return false;
        rear = (rear + 1) % maxSize;
        data[rear] = value;
        return true;
    }
    
    public boolean deQueue() {
        if(isEmpty())
            return false;
        if(front == rear){
            front = 0;
            rear = -1;
        }
        else {
            front = (front + 1) % maxSize;
        }
        
        return true;
    }
    
    public int Front() {
        return isEmpty() ? -1 : data[front];
    }
    
    public int Rear() {
        return isEmpty() ? -1 : data[rear];
    }
    
    public boolean isEmpty() {
        return rear == -1;
    }
    
    public boolean isFull() {
        if (!isEmpty() && (rear+1)%maxSize == front)
            return true;
        return false;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */