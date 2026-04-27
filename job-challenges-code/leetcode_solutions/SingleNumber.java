class MySolution {
    public int singleNumber(int[] nums) {
        int singleOne = 0;
        int size = nums.length;
        Map<Integer, Integer> numbersMap = new HashMap<>();

        if (size == 1) {
            return nums[0];
        }

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                numbersMap.put(nums[j], 1);
           }
            if (numbersMap.get(nums[i]) != null) {
                numbersMap.put(nums[i], numbersMap.get(nums[i]) + 1);
                // numbersMap.put(nums[i], numbersMap.get(nums[i + 1])+ 1);
            }
        }
        System.out.println(numbersMap);
        return numbersMap.values().iterator().next();
    }
}

class CommunitySolution {
     public int singleNumber(int[] nums) {
        int res = 0;

        for (int n : nums) {
            res ^= n;
        }

        return res;
     }

    //  Second solution in Python
    // return 2 * sum(set(nums)) - sum(nums);

    // [2, 1, 2, 3, 1]
    // [2, 1, 3] = 6 * 2 = 12
    // [1, 1, 2, 2, 3, 3]
    // [1, 1, 2, 2, 3] = 3
}
