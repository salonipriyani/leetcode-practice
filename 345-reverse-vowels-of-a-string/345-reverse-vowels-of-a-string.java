class Solution {
    public String reverseVowels(String s) {
        char[] sChars = s.toCharArray();
        String vowels = "aeiouAEIOU";
        int left = 0;
        int right = sChars.length - 1;
        char temp;
        while(left < right){
            if (vowels.indexOf(sChars[left]) == -1){
                left++;
                continue;
            }
            else if(vowels.indexOf(sChars[right]) == -1){
                right--;
                continue;
            }
            temp = sChars[left];
            sChars[left] = sChars[right];
            sChars[right] = temp;
            left++;
            right--;
        }
        return String.valueOf(sChars);
    }
}