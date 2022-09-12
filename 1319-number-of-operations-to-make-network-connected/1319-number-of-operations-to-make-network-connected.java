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
        
        //2. DFS to get number of components
        boolean[] visited = new boolean[n];
        for (int i = 0; i< n; i++){
            if(!visited[i]){
                dfs(adj, visited, i);
                c++;
            }
        }
        //find no. of redundancies
        //if c = 1, r = e - (n-1) -> edges minus number of edges required to connect n nodes
        
        int r = e - ((n-1)-(c-1)); //number of redundancies
        
        if (r < c-1)
            return -1;
        //number of edges required to join the components
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