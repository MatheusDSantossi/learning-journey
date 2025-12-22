class Solution {
    public int jump(int[] nums) {
        int gas = 0;
        int steps = 0;
        int firstStep = nums[0];

        if (nums.length == 1) {
            return steps;
        }

        if (firstStep >= nums.length - 1) {
            return 1;
        }

        for (int n : nums) {
            if (gas < nums.length - 1 && n != 0) {
                gas += n;
                steps++;
            }
        }

        return steps;
    }
}

class CommunitySolution {
    public int jump(int[] nums) {
        int ans = 0; // number of minimum jumps taken
        int end = 0; // end of the current jump range
        int farthest = 0; // farthest index we can reach from current

        // we stop at nums.length -1 because once we reach or pass it, we're done
        for (int i = 0; i < nums.length -1; ++i) {
            // update the farthest reachable index from the position
            farthest = Math.max(farthest, i + nums[i]);

            // if we can already reach por passs the last index,
            // take one more jump and finish
            if(farthest >= nums.length - 1) {
                ++ans;
                break;
            }

            // When we've iterated through the current "level" (jump range),
            // it's time to make next jump
            if (i == end) {
                ++ans; // increase the jump count
                end = farthest; // update the boundry for the next level
            }
        }

        return ans;
    }
}
