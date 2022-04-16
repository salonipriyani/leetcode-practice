class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s==null || s.length()==0){
            return 0;
        }
        HashMap<Character, Integer> map = new HashMap<>();
        int start =0;
        int longestIndex[] = new int[]{0,1};
        for(int i=0;i<s.length();i++){
            Character atIndex = s.charAt(i);
            if(map.containsKey(atIndex)){
                start = Math.max(start, map.get(atIndex) +1 );
            }
            if(longestIndex[1] - longestIndex[0] < i+1 - start){
                longestIndex[0] = start;
                longestIndex[1] = i+1;
            }
            map.put(atIndex, i);
        }
        return longestIndex[1] - longestIndex[0];
        
    }
}