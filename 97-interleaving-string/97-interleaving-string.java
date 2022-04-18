class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        
        int M = s1.length();
        int N = s2.length();
        boolean[][] dp = new boolean[M+1][N+1];
        
        if (M+N != s3.length())
            return false;
        
        for (int i = 0; i <= M; i++){
            for (int j = 0; j <= N; j++){
                if (i == 0 && j == 0)
                    dp[i][j] = true;
                
                else if (i == 0){
                    if (s2.charAt(j - 1) == s3.charAt(j-1))
                        dp[i][j] = dp[i][j - 1];
                }   
                
                else if (j == 0){
                    if (s1.charAt(i-1) == s3.charAt(i - 1))
                        dp[i][j] = dp[i - 1][j];
                }
                    
                
                else if (s1.charAt(i - 1) == s3.charAt(i +j - 1) && s2.charAt(j - 1) != s3.charAt(i +j - 1))
                    dp[i][j] = dp[i - 1][j];
                
                else if (s2.charAt(j - 1) == s3.charAt(i +j - 1) && s1.charAt(i - 1) != s3.charAt(i +j - 1))
                    dp[i][j] = dp[i][j - 1];
                
                else if (s1.charAt(i - 1) == s3.charAt(i +j - 1) && s2.charAt(j - 1) == s3.charAt(i +j - 1))
                    dp[i][j] = dp[i - 1][j] || dp[i][j - 1];
            }
        }
        
        
      return dp[M][N];
    }
}