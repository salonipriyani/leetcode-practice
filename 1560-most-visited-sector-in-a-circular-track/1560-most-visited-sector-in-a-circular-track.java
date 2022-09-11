class Solution {
    public List<Integer> mostVisited(int n, int[] rounds) {
        List<Integer> ls = new ArrayList<>();
        if (rounds[0] <= rounds[rounds.length - 1]){
            for (int i = rounds[0]; i <= rounds[rounds.length - 1]; i++)
                ls.add(i);
        }
        else{
            for(int i = 1; i <= n; i++){
                if(i == rounds[rounds.length - 1] + 1)
                    i = rounds[0];
                ls.add(i);
            }
                
            
        }
        
        return ls;
    }
}