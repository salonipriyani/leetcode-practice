class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // map each course to empty prereq lisrt
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < numCourses; i++){
            map.put(i, new ArrayList<>());
        }
        
        for (int[] prereq : prerequisites){
            int course = prereq[0];
            int pre = prereq[1];
            List<Integer> l = map.get(course);
            l.add(pre);
            map.put(course, l);
        }
        
        // visitSet = all courses along current dfs path
        Set<Integer> visitSet = new HashSet<>();
        
        for (int i = 0; i < prerequisites.length; i++){
            if (dfs(prerequisites[i][0], visitSet, map) == false)
                return false;
        }
        return true;
    }
    
    public boolean dfs (int course, Set<Integer> visitSet, Map<Integer, List<Integer>> map){
        if (visitSet.contains(course))
            return false;
        if (map.get(course).isEmpty())
            return true;
        visitSet.add(course);
        for (int pre : map.get(course)){
            if (dfs(pre, visitSet, map) == false)
                return false;
        }
        
        visitSet.remove(course);
        map.put(course, new ArrayList<>());
        return true;
    }
}