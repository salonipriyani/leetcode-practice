class Solution {
    
    Map<Integer, List<Integer>> map = new HashMap();
    List<Integer> ans = new ArrayList<>();
    Set<Integer> visit = new HashSet<>(), cycle = new HashSet<>();
    
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // map course to prereqs
        for (int i = 0; i < numCourses; i++){
            map.put(i, new ArrayList<>());
        }
        for (int[] pair : prerequisites){
            int course = pair[0];
            int prereq = pair[1];
            List<Integer> l = map.get(course);
            l.add(prereq);
            map.put(course, l);
        }
        
        for (int i = 0; i < numCourses; i++){
            if (dfs(i) == false)
                return new int[0];
        }
        
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
    
    public boolean dfs(int course){
        if (cycle.contains(course))
            return false;
        if (visit.contains(course))
            return true;
        
        cycle.add(course);
        for (int prereq : map.get(course)){
            if (dfs(prereq) == false)
                return false;
        }
        
        cycle.remove(course);
        visit.add(course);
        ans.add(course);
        return true;
    }
}