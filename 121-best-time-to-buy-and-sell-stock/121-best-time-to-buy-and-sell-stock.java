class Solution {
    public int maxProfit(int[] prices) {
        int lsf = Integer.MAX_VALUE; //leastSOFar
        int overallProfit = 0;
        int pist = 0; //profit if sold today
        
        for (int i = 0; i < prices.length; i++){
            if(prices[i] < lsf)
                lsf = prices[i];
            pist = prices[i] - lsf;
            
            if(overallProfit < pist)
                overallProfit = pist;
        }
        
        return overallProfit;
    }
}