class Solution {
    public int maxProfit(int[] prices) {
        int buyPrice = prices[0];
        int sellPrice = 0;
        int profit = 0;
        int pointerAllowed = 0;

        for (int i = 1; i <= prices.length - 1; i++) {
            if (prices[i] < buyPrice) {
                pointerAllowed = i;
                buyPrice = prices[i];
            }
            
            if (prices[i] > sellPrice && i > pointerAllowed) {
                if (i < prices.length - 1) {
                    if (prices[i] > prices[i + 1]) {
                        sellPrice = prices[i];
                    } else {
                        sellPrice = prices[i + 1];

                    }
                } else {

                        sellPrice = prices[i];
                }
            }
            
            if (buyPrice < sellPrice) {
                profit += Math.max(buyPrice, sellPrice - buyPrice);
                buyPrice = 99999;
                sellPrice = 0;
            }
        }

        return profit;
    }
}

class CorrectSolutionSolved {
    public int maxProfit(int[] prices) {
        int max = 0;
        int start = prices[0];
        int len = prices.length;

        for (int i = 1; i < len; i++) {
            if (start < prices[i]) max += prices[i] - start;

            start = prices[i];
        }

        return max;
    }
}
