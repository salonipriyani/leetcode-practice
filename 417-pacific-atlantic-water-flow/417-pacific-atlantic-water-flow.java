//DFS
class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        //resulting list
        List<List<Integer>> res = new ArrayList<>();
        
        //base conditions
        if (heights == null || heights.length == 0 || heights[0].length == 0)
            return res;
        
        //declaring boolean matrices of squares that can empty
        //into respective oceans
        int rows = heights.length, cols = heights[0].length;
        boolean[][] pacific = new boolean[rows][cols];
        boolean[][] atlantic = new boolean[rows][cols];
        
        for (int c = 0; c < cols; c++){
            dfs(heights, pacific, Integer.MIN_VALUE, 0, c);
            dfs(heights, atlantic, Integer.MIN_VALUE, rows - 1, c);
        }
        
        for (int r = 0; r < rows; r++){
            dfs(heights, pacific, Integer.MIN_VALUE, r, 0);
            dfs(heights, atlantic, Integer.MIN_VALUE, r, cols - 1);
        }
        
        for (int r = 0; r < rows; r++){
            for (int c = 0; c < cols; c++){
                if (pacific[r][c] && atlantic[r][c]){
                    res.add(Arrays.asList(r,c));
                }
            }
        }
        return res;
    }
    
    public void dfs(int[][] heights, boolean[][] visited, int prevHeight, int row, int col){
        int rows = heights.length;
        int cols = heights[0].length;
        if (row < 0 || col < 0 || row == rows || col == cols || visited[row][col]
           || heights[row][col] < prevHeight)
            return;
        visited[row][col] = true;
        dfs(heights, visited, heights[row][col], row + 1, col);
        dfs(heights, visited, heights[row][col], row - 1, col);
        dfs(heights, visited, heights[row][col], row, col + 1);
        dfs(heights, visited, heights[row][col], row, col - 1);
    }
}