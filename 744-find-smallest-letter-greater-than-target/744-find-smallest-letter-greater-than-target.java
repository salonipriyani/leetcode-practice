class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int start = 0, end = letters.length - 1;
        char ans = letters[0];
        while (start <= end){
            int mid = (start + end)/2;
            if (letters[mid] > target){
                end = mid - 1;
                ans = letters[mid];
            }
            else
                start = mid + 1;
                
        }
        
        return ans;
    }
}