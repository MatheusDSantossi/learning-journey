class MySolution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        
        int gasSum = Arrays.stream(gas).sum();
        int costSum = Arrays.stream(cost).sum();

        int start = 0;
        int tank = 0;

        for (int i = 0; i < cost.length; i++) {
            for (int j = 0; j < gas.length; j++) {
                if (gas[j] >= cost[i] && start != 0) {
                    start = j;
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