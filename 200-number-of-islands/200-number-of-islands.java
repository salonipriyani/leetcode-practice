//BFS
class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length, cols = grid[0].length, count = 0;
        boolean[][] visited = new boolean[rows][cols];
        Queue<int[]> q = new LinkedList<>();
        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++){
                if (grid[i][j] == '1' && !visited[i][j]){
                    q.offer(new int[]{i, j});
                    visited[i][j] = true;
                    bfs(grid, visited, q);
                    count++;
                }
            }
        }
        return count;
    }
    int[][] dirs = new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    public void bfs(char[][] grid, boolean[][] visited, Queue<int[]> q){
        int rows = grid.length, cols = grid[0].length;
        while(!q.isEmpty()){
            int[] cur = q.poll();
            for (int[] dir : dirs){
                int x = cur[0] + dir[0];
                int y = cur[1] + dir[1];
                if (x < 0 || y < 0 || x >= rows || y >= cols || visited[x][y] || grid[x][y] == '0')
                    continue;
                
                visited[x][y] = true;
                q.offer(new int[]{x, y});
            }
        }
    }
}