 class Solution {
    public int lengthOfLongestSubstring(String s) {
        int ans = 0;
        HashMap<Character,Integer> map = new HashMap<>();
        
        int acq = 0;
        int rl = 0;
        
        for(;acq < s.length();acq++){
            char cur = s.charAt(acq);
            
            while(map.containsKey(cur)){
                map.remove(s.charAt(rl));
                rl++;
            }
            
            map.put(cur,1);
            
            ans = Math.max(ans,(acq - rl) + 1);
        }
        
        return ans;
    }
}