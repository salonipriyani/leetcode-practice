class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int start = 0, end = arr.length - 1;
        int ans = -1;
        while (start < end){
            int mid = (start + end)/2;
            if (arr[mid] > arr[mid + 1])
                end = mid;
            else
                start = mid + 1;
        }
        
        return start;
    }
}