class Solution {
    public int findKthPositive(int[] arr, int k) {
        int i = 0;
        while (i < arr.length){
            int j = arr[i] - 1;
            if (arr[i] <= arr.length && arr[i] != arr[j])
                swap(arr, i, j);
            else
                i++;
        }
        List<Integer> missingNumbers = new ArrayList<>();
        Set<Integer> extraNumbers = new HashSet<>();
        for (i = 0; i < arr.length && missingNumbers.size() < k; i++){
            if (arr[i] != i+1){
                missingNumbers.add(i+1);
                extraNumbers.add(arr[i]);
            }
        }
        
        for (i = 1; missingNumbers.size() < k; i++){
            int candidate = i + arr.length;
            if (!extraNumbers.contains(candidate))
                missingNumbers.add(candidate);
        }
        
        return missingNumbers.get(k-1);
    }
    
    private void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}