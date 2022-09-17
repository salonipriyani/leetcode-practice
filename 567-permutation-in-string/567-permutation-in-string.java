class Solution {
    public boolean checkInclusion(String s1, String s2) {
        
        //1. create character freq map for the pattern
        Map<Character, Integer> freqMap = new HashMap<>();
        for (int i = 0; i < s1.length(); i++){
            char curr = s1.charAt(i);
            freqMap.put(curr, freqMap.getOrDefault(curr, 0) + 1);
        }
        
        int windowStart = 0, matched = 0;
        for (int windowEnd = 0; windowEnd < s2.length(); windowEnd++){
            char curr = s2.charAt(windowEnd);
            if (freqMap.containsKey(curr)){
                freqMap.put(curr, freqMap.get(curr) - 1);
                if (freqMap.get(curr) == 0)
                    matched++;
            }
            
            if (matched == freqMap.size())
                return true;
        
            if (windowEnd -windowStart + 1 >= s1.length()){
                char left = s2.charAt(windowStart);
                windowStart++;
                if (freqMap.containsKey(left)){
                    if (freqMap.get(left) == 0)
                        matched--;
                    freqMap.put(left, freqMap.get(left) + 1);
                }
                
            }
        }
        
        return false;
    }
    
}