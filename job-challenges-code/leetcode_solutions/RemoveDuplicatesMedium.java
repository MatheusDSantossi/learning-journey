class Solution {
    public int removeDuplicates(int[] nums) {
        int k = nums.length;
        int pointer = 0;
        int doubleDuplicated = 0;

        for (int i = 2; i < nums.length; i++) {
            if (nums[i] == nums[pointer]) {
                nums[i] = nums[i + 1];
                k--;
            }
            pointer++;
        }
        System.out.println(Arrays.toString(nums));
        return k + 1;
    }
}

class OtherStudentSolution {

    public int removeDuplicates(int[] nums) {
        int n = nums.length;

        if (n < 3)
            return n;
        int a = 2;

        for (int i = 2; i < n; i++) {
            if (nums[i] != nums[a - 2]) {
                nums[a] = nums[i];
                a++;
            }
        }

        return a;
    }

}
