class MySolution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        
        int gasSum = Arrays.stream(gas).sum();
        int costSum = Arrays.stream(cost).sum();

        int start = -1;
        int tank = 0;

        for (int i = 0; i < cost.length; i++) {
            for (int j = 0; j < gas.length; j++) {
                if (gas[j] >= cost[i]) {
                    if (j != 0 || j != gas.length) {
                        start = j;

                    }
                } 
            }
        }
        
        if (costSum > gasSum) {
            return -1;
        } 
        return start;

        //     if (i == 0) {
        //         tank = gas[start];
        //         tank = tank - cost[start] + gas[start]; 
        //     } else {
        //         tank = gas[i];
        //         tank = tank - cost[i] + gas[i];
        //     }
        // } 
        // return tank;
        // if (tank > 0) {
        //     return start;        
        // }
        // return - 1;
    }
}

class CommunitySolution {
    class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        int total_surplus = 0;
        int surplus = 0;
        int start = 0;

        for (int i = 0; i < n; i++) {
            total_surplus += gas[i] - cost[i];
            surplus += gas[i] - cost[i];
            if (surplus < 0) {
                surplus = 0;
                start = i + 1;
            }
        }
        return (total_surplus < 0) ? -1 : start;
    }
}
}
