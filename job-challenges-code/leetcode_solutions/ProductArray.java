class SimplestAnswer() {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];

        for (int i = 0; i < n; i++) {
            int pro = 1;
            for (int j = 0; j < n; j++) {

            if (i == j) continue;
            pro *= nums[j];
            }
        answer[i] = pro;
        }

        return answer;
    }
}

class EfficientAnswer() {
     public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];

        Arrays.fill(answer, 1);
        int curr = 1;

        for (int i = 0; i < n; i++) {
            answer[i] *= curr;
            curr *= nums[i];
        } 

        curr = 1;
        
        for (int i = n -1; i >= 0; i--) {
            answer[i] *= curr;
            curr *= nums[i];
        }

        return answer;
}
