class Solution {
    public int hIndex(int[] citations) {
        int total = 0;

        if (citations[0] == 0 && citations.length == 1) {
            return 0;
        }

        if (citations.length == 1) {
            return 1;
        }

        for (int i = 0; i < citations.length; i++) {
            total += citations[i];
        }

        if (total == 0) {
            return 0;
        }
        
        int hIndex = total / citations.length;
        if (hIndex > citations.length) {
            return citations.length;
        }
        return (hIndex > 0) ? hIndex : 1;
    }
}

class CommunitySolution {
    public int hIndex(int[] citations) {
        int n = citations.length;
        int[] buckets = new int[n + 1]; // buckets will be the size of citations + 1

        for (int c : citations) {
        if (c >= n) {
            buckets[n]++;
        } else {
            buckets[c]++;
        }
    }

    int count = 0;
    for (int i = n; i >= 0; i--) {
        count += buckets[i];
        if (count >= i) {
            return i;
        }
    }

    return 0;
    }

}
