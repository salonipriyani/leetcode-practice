class Solution {
    public int compress(char[] chars) {
        int count = 1;
        int index = 0; 
        for(int i =0; i < chars.length; i++) {
            if (i+1 == chars.length || chars[i] != chars[i+1]){
                chars[index++] = chars[i];
                if (count != 1){
                    for(char a : Integer.toString(count).toCharArray())
                        chars[index++] = a;
                    count = 1;
                }
            }
            else
                count++;
        }
        return index;
    }
}