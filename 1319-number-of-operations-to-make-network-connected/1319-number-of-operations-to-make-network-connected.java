class Solution {
    public int makeConnected(int n, int[][] connections) {
        //1. Make an adjacency list
        List<List<Integer>> adj = new ArrayList<>();
        int e = connections.length; //edges
        int c = 0; //no. of components --> through DFS
        if (e < n-1)
            return -1;
        for (int i = 0; i < n; i++)
            adj.add(new ArrayList<>());
        
        for (int[] connection: connections){
            adj.get(connection[0]).add(connection[1]);
            adj.get(connection[1]).add(connection[0]);
        }
        
        //DFS
        boolean[] visited = new boolean[n];
        for (int i = 0; i< n; i++){
            if(!visited[i]){
                dfs(adj, visited, i);
                c++;
            }
        }
        
        int r = e - ((n-1)-(c-1)); //number of redundancies
        
        if (r < c-1)
            return -1;
        return c-1;
    }
    
    public void dfs(List<List<Integer>> adj, boolean[] visited, int i){
        if (visited[i])
            return;
        
        visited[i] = true;
        List<Integer> neighbours = adj.get(i);
        for (int n: neighbours){
            if (!visited[n])
                dfs(adj, visited, n);
        }
    }
}