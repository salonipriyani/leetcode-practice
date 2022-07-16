class Solution {
    public List<String> letterCasePermutation(String s) {
        List<String> permutations = new ArrayList<>();
        if (s == null)
            return permutations;
        
        permutations.add(s);
        for (int i = 0; i < s.length(); i++){
            char curr = s.charAt(i);
            if(Character.isLetter(curr)){
                int size = permutations.size();
                for(int j = 0; j < size; j++){
                    char[] currStr = permutations.get(j).toCharArray();
                    if (Character.isUpperCase(currStr[i]))
                        currStr[i] = Character.toLowerCase(currStr[i]);
                    else
                        currStr[i] = Character.toUpperCase(currStr[i]);
                    permutations.add(String.valueOf(currStr));
                }
            }
        }
        
        return permutations;
    }
}