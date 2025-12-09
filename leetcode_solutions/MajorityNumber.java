class SolutionUsingHashMap {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> hash = new HashMap<>();
        int res = 0;
        int majority = 0;
        
        for (int n : nums) {
            hash.put(n, 1 + hash.getOrDefault(n, 0));
            if (hash.get(n) > majority) {
                res = n;
                majority = hash.get(n);
            }

        }

        return res;

    }
}

class SolutionUsingLinearMethod {
    public int majorityElement(int[] nums) {
        int res = 0;
        int majority = 0;
        
        for (int n : nums) {
            if (majority == 0) {
                res = n;
            }

            if (n == res) {
                majority++;
            } else {
                majority--;
                }

        }

        return res;

    }
}
