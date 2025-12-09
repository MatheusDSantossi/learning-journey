class MyIncompleteSolution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int min = 99999;
        int pointerAllowed = 0;
        int maxPointer = 0;

        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < min && i < prices.length - 1) {
                pointerAllowed = i;
                min = prices[i];
            }

            if (i >= prices.length - 1 && maxPointer > pointerAllowed) {
                pointerAllowed = i + 1;
            }
            if (prices[i] > max && i > pointerAllowed) {
                maxPointer = i;
                max = prices[i];
            }

        }

        System.out.println(pointerAllowed);

        if (pointerAllowed == prices.length - 1) {
            return 0;
        }

        return max - min;

    }
}

class SolvedSolution {
    public int maxProfit(int[] prices) {
        int buyPrice = prices[0];
        int profit = 0;

        for (int i = 1; i < prices.length; i++) {
            if (buyPrice > prices[i]) {
                buyPrice = prices[i];
            }

            profit = Math.max(profit, prices[i] - buyPrice);
        }

        return profit;

    }
}
