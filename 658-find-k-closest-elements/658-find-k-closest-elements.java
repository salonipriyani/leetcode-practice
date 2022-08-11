class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int start = 0, end = arr.length - 1;
        while (end - start >= k){
            int mid = (start + end)/2;
            if (Math.abs(arr[end] - x) < Math.abs(arr[start] - x))
                start++;
            else
                end--;
        }
        List<Integer> result = new ArrayList<>();
        for (int i = start; i <= end; i++){
            result.add(arr[i]);
        }
        return result;
    }
}