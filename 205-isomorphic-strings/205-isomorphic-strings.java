class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length())
            return false;
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();
        Map<Character, Character> iso = new HashMap<>();
        iso.put(sChars[0], tChars[0]);
        for (int i = 1; i < sChars.length; i++){
            if (iso.containsKey(sChars[i])){
                if (iso.get(sChars[i]) != tChars[i])
                    return false;
            }
            else if(iso.containsValue(tChars[i]))
                return false;
            else {
                iso.put(sChars[i], tChars[i]);
            }
        }
        return true;
    }
}