class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer, Integer> fruitFreq = new HashMap<>();
        int windowStart = 0, maxLen = Integer.MIN_VALUE;
        for (int windowEnd = 0; windowEnd < fruits.length; windowEnd++){
            fruitFreq.put(fruits[windowEnd], fruitFreq.getOrDefault(fruits[windowEnd], 0) + 1);
            while (fruitFreq.size() > 2){
                fruitFreq.put(fruits[windowStart], fruitFreq.get(fruits[windowStart]) - 1);
                if (fruitFreq.get(fruits[windowStart]) == 0)
                    fruitFreq.remove(fruits[windowStart]);
                windowStart++;
            }
            maxLen = Math.max(maxLen, windowEnd - windowStart + 1);
            
        }
        return maxLen;
    }
}