class Solution {
    public boolean checkInclusion(String s1, String s2) {
        
        if (s1.length() > s2.length())
            return false;
        int[] s1Char = new int[26];
        int[] s2Char = new int[26];
        
        for(int i = 0; i < s1.length(); i++){
            s1Char[s1.charAt(i) - 'a']++;
            s2Char[s2.charAt(i) - 'a']++;
        }
        int windowStart = 0;
        int windowEnd = s1.length();
        while(windowEnd < s2.length()){
            if (matches(s1Char, s2Char))
                return true;
            
            s2Char[s2.charAt(windowStart) - 'a']--;
            s2Char[s2.charAt(windowEnd) - 'a']++;
            
            windowStart++;
            windowEnd++;
        }
        
        if (matches(s1Char, s2Char))
            return true;
        return false;
    }
    
    private boolean matches(int[] s1Char, int[] s2Char){
        for(int i = 0; i < 26; i++){
            if (s1Char[i] != s2Char[i])
                return false;
        }
        return true;
    }
}