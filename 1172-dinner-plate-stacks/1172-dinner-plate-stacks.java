class DinnerPlates {
    
    int capacity;
    List<Stack<Integer>> stackList;
    PriorityQueue<Integer> leftPushableStacks;
    public DinnerPlates(int capacity) {
        this.capacity = capacity;
        stackList = new ArrayList<>();
        leftPushableStacks = new PriorityQueue<>();
    }
    
    public void push(int val) {
        if(leftPushableStacks.isEmpty()){
            Stack<Integer> newStack = new Stack<>();
            newStack.push(val);
            stackList.add(newStack);
            
            if (capacity > 1)
                leftPushableStacks.add(stackList.size() - 1);
        }
        else {
            Stack<Integer> pushStack = stackList.get(leftPushableStacks.peek());
            pushStack.push(val);
            if(pushStack.size() == capacity)
                leftPushableStacks.poll();
        }
    }
    
    public int pop() {
        for (int i = stackList.size() - 1; i > -1 && stackList.get(i).empty(); i--){
            stackList.remove(i);
            leftPushableStacks.remove(i);
        }
        return popAtStack(stackList.size() - 1);
    }
    
    public int popAtStack(int index) {
        if (index < 0 || index >= stackList.size())
            return -1;
        
        Stack<Integer> targetStack = stackList.get(index);
        
        if(targetStack.isEmpty())
            return -1;
        if(targetStack.size() == capacity)
            leftPushableStacks.add(index);
        
        return targetStack.pop();
    }
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * DinnerPlates obj = new DinnerPlates(capacity);
 * obj.push(val);
 * int param_2 = obj.pop();
 * int param_3 = obj.popAtStack(index);
 */