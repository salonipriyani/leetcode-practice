class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] isTrusted = new int[n+1];
        for(int[] persons: trust){
            isTrusted[persons[0]] -= 1;
            isTrusted[persons[1]] += 1;
        }
        for (int i = 1; i <= n; i++){
            if (isTrusted[i] == n-1)
                return i;
        }
        
        return -1;
    }
}