class MySolution {
    public int singleNumber(int[] nums) {
        int r = 0;
        Map<Integer, Integer> numbersMap = new HashMap<>();

        for (int n : nums) {
            numbersMap.put(n, numbersMap.getOrDefault(n, 0) + 1);
        }
        System.out.println(numbersMap);

        Integer keyWithOne = numbersMap.entrySet().stream().filter(entry -> entry.getValue() == 1)
                .map(Map.Entry::getKey).findFirst().orElse(null);
        return keyWithOne;
    }
}

// using bit manipulation
class CommunitySolution {
    public int singleNumber(int[] nums) {
        int ans = 0;

        for (int i = 0; i < 32; ++i) {
            int sum = 0;
            for (final int num : nums) {
                sum += num >> i & 1;
            }
            sum %= 3;
            ans |= sum << i;
        }
        // TEST
        return ans;
    }
}
