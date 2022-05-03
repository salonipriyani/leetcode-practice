class Solution {
    public int characterReplacement(String s, int k) {
        int left = 0;
        int maxRepeatChar = 0, max = 0;
        Map<Character, Integer> map = new HashMap<>();
        for(int right = 0; right < s.length(); right++){
            char c = s.charAt(right);
            map.put(c, map.getOrDefault(c, 0) + 1);
            maxRepeatChar = Math.max(maxRepeatChar, map.get(c));
            int maxRepeatCharWindow = right - left + 1;
            if (maxRepeatCharWindow - maxRepeatChar > k){
                char leftChar = s.charAt(left);
                map.put(leftChar, map.get(leftChar) - 1);
                left++;
            }
            max = Math.max(max, right - left + 1);
        }
        return max;
    }
}