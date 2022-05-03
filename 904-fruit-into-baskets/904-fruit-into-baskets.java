class Solution {
    public int totalFruit(int[] fruits) {
        int sum = 0, left = 0, temp;
        Map<Integer, Integer> map = new HashMap<>();
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < fruits.length; i++){
            map.put(fruits[i], map.getOrDefault(fruits[i], 0) + 1);
            sum++;
            
            if(map.size() > 2){
                while(map.size() > 2){
                    if(map.containsKey(fruits[left])){
                        if(map.get(fruits[left]) == 1)
                            map.remove(fruits[left]);
                        else
                            map.put(fruits[left], map.get(fruits[left]) - 1);
                    }
                    left++;
                    sum--;
                }
            }
            else {
                max = Math.max(max, sum);
            }
            
        }
        return max;
    }
}