class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        for(int[] edge: edges){
            int node0 = edge[0];
            int node1 = edge[1];
            List<Integer> l0 = map.getOrDefault(node0, new ArrayList<>());
            List<Integer> l1 = map.getOrDefault(node1, new ArrayList<>());
            l0.add(node1);
            l1.add(node0);
            map.put(node0, l0);
            map.put(node1, l1);
        }
        
        boolean[] visited = new boolean[n];
        Queue<Integer> q = new LinkedList<>();
        q.offer(source);
        visited[source] = true;
        while(!q.isEmpty()){
            int node = q.poll();
            if(node == destination)
                return true;
            List<Integer> l = map.getOrDefault(node, new ArrayList<>());
            for(int a : l){
                if(!visited[a]){
                    visited[a] = true;
                    q.offer(a);
                }
            }
        }
        
        return false;
    }
}