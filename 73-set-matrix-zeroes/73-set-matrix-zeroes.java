class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        boolean[][] isZero = new boolean[m][n];
        int i, j;
        
        for (i = 0; i < m; i++){
            for (j = 0;  j < n; j++){
                if(matrix[i][j] == 0)
                    isZero[i][j] = true;
            }
        }
        
        for (i = 0; i< m; i++){
            for (j = 0; j < n; j++){
                if (isZero[i][j] == true){
                    makeRowZero(matrix, i, n);
                    makeColumnZero(matrix, j, m);
                }
            }
        }
        
        
    }
    
    public void makeRowZero(int[][] matrix, int i, int n){
        for(int k = 0; k < n; k++){
            matrix[i][k] = 0;
        }
    }

    public void makeColumnZero(int[][] matrix, int j, int m){
        for(int k = 0; k < m; k++){
            matrix[k][j] = 0;
        }
    }
}