class MyCircularDeque {
    
    int maxSize, front, rear;
    int[] data;

    public MyCircularDeque(int k) {
        data = new int[k];
        front = -1;
        rear = -1;
        maxSize = k;
    }
    
    public boolean insertFront(int value) {
        if (isFull())
            return false;
        if (front == -1){
            front = 0;
            rear = 0;
        }
            
        else if (front == 0)
            front = maxSize - 1;
        else
            front--;
        data[front] = value;
        return true;
    }
    
    public boolean insertLast(int value) {
        if (isFull())
            return false;
        if (front == -1){
            front = 0;
            rear = 0;
        }
        else if (rear == maxSize - 1)
            rear = 0;
        else
            rear++;
        data[rear] = value;
        return true;
    }
    
    public boolean deleteFront() {
        if (isEmpty())
            return false;
        if(front == rear){
            front = -1;
            rear = -1;
        } 
        else {
            if (front == maxSize - 1)
                front = 0;
            else
                front++;
        }
        return true;
    }
    
    public boolean deleteLast() {
        if (isEmpty())
            return false;
        if(front == rear){
            front = -1;
            rear = -1;
        } 
        else if (rear == 0)
            rear = maxSize - 1;
        else
            rear--;
        return true;
    }
    
    public int getFront() {
        return isEmpty() ? -1 : data[front];
    }
    
    public int getRear() {
        return isEmpty() ? -1 : data[rear];
    }
    
    public boolean isEmpty() {
        return (front == -1);
    }
    
    public boolean isFull() {
        return ((front == 0 && rear == maxSize - 1) || (front == rear + 1));
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */