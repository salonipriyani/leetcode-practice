class Solution {
    public int maxProfit(int[] prices) {
        int i;
        for (i = prices.length - 1; i > 0; i--)
            prices[i] = prices[i] - prices[i - 1]; 
        
        int sumTillHere = 0;
        int maxSoFar = Integer.MIN_VALUE;
        
        for (i = 1; i < prices.length; i++){
            sumTillHere += prices[i];
            if (maxSoFar < sumTillHere)
                maxSoFar = sumTillHere;
            if (sumTillHere < 0)
                sumTillHere = 0;
        }
        if(maxSoFar < 0)
            return 0;
        return maxSoFar;
    }
}