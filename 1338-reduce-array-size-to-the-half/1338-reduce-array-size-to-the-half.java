class Solution {
    public int minSetSize(int[] arr) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int i = 0; i < arr.length; i++){
            freq.put(arr[i], freq.getOrDefault(arr[i], 0) + 1);
        }
        Set<Integer> intMax = new HashSet<>();
        List<Integer> counts = new ArrayList<>(freq.values());
        Collections.sort(counts);
        Collections.reverse(counts);
        
        int numbersRemovedFromArr = 0;
        int setSize = 0;
        for (int count : counts){
            numbersRemovedFromArr += count;
            setSize++;
            if (numbersRemovedFromArr >= arr.length/2)
                break;
        }
        
        return setSize;
    }
}