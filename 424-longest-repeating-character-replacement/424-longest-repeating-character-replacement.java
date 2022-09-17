class Solution {
    public int characterReplacement(String s, int k) {
        //windowEnd - windowStart + 1 -> answer - > to be maximized
        int windowStart = 0, max = Integer.MIN_VALUE, maxRepeatingChar = 0;
        Map<Character, Integer> map = new HashMap<>();
        for (int windowEnd = 0; windowEnd < s.length(); windowEnd++){
            char curr = s.charAt(windowEnd);
            map.put(curr, map.getOrDefault(curr, 0) +1);
            maxRepeatingChar = Math.max(maxRepeatingChar, map.get(curr));
            int windowSize = windowEnd - windowStart + 1;
            if (windowSize - maxRepeatingChar > k){
                char leftChar = s.charAt(windowStart);
                map.put(leftChar, map.get(leftChar) - 1);
                windowStart++;
            }
            max = Math.max(max, windowEnd - windowStart + 1);
        }
        
        return max;
    }
}