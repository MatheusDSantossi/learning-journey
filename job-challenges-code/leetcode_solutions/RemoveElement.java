package leetcode_solutions;

import java.util.Arrays;

// this solution is working, however it took 2ms (runtime) and 42.35 MB of memory
public class RemoveElement {
    public int removeElement(int[] nums, int val) {
        // int k = nums.length; // elements of the new array after removing numbers
        // necessary
        int k = 0; // elements of the new array after removing numbers necessary

        // int pointer = nums.length - 1;
        int pointer = 0;
        int shiftLeft = nums.length - 1;

        while (pointer < nums.length) {
            if (nums[pointer] != val) {
                nums[k] = nums[pointer];
                k += 1;
            } else {
                // nums[shiftLeft] = nums[pointer];
                nums[pointer] = 0;
                shiftLeft--;
            }

            // pointer -= 1;
            pointer += 1;
        }

        System.out.println(Arrays.toString(nums));
        return k;

    }
}

class RemoveElementSolution {
    public int removeElement(int[] nums, int val) {
        int i = 2;

        return i;
    }
}
