
import java.util.Arrays;

class Solution {
    public int removeDuplicates(int[] nums) {
        int previousNumber = 0;
        int pointer = 1;
        int k = nums.length;

        if (k == 1) {
            return k;
        }

        // While previousNumber isn't in the end of the list
        while (previousNumber <= nums.length - 1) {
            if (nums[previousNumber] == nums[pointer]) {
                nums[previousNumber] = 101;
                k--;
                previousNumber++;
            }

            if (pointer == nums.length - 1 && previousNumber < nums.length - 1) {
                previousNumber++;
                pointer = previousNumber;
            }

            if (previousNumber == nums.length - 1) {
                break;
            }
            pointer++;
        }
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));
        return k;
    }
}

class SolutionProfessor {
    public int removeDuplicates(int[] nums) {
        int k = nums.length;
        int pointer = 1;

        if (k == 1) {
            return k;
        }

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[pointer - 1]) {
                nums[pointer] = nums[i];
                pointer++;
                // k--;
            }
        }

        System.out.println(Arrays.toString(nums));
        return pointer;

    }
}
