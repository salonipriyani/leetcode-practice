class Solution {
    public void rotate(int[][] matrix) {
        //Rotate Image algorithm
        //1. Transpose of matrix
        //2. reverse rows
        int temp, i, j;
        for (i=0; i < matrix.length; i++){
            for (j=i; j < matrix[0].length; j++){
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        
        for (i=0; i<matrix.length; i++) {
            int left = 0;
            int right = matrix[i].length - 1;
            while(left < right){
                temp = matrix[i][left];
                matrix[i][left] = matrix[i][right];
                matrix[i][right] = temp;
                left++;
                right--;
            }
        }
        
    }
}