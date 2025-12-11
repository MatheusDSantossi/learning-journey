// Not completely correct
class Solution {
    public boolean canJump(int[] nums) {
        int firstStep = nums[0];
        if (firstStep > nums.length) return false;
        if (firstStep == nums.length || firstStep == nums.length - 1) {
            return true;
        }
        if (nums.length == 1) {
            return true;
        }
        int step = nums[firstStep];

        for (int i = firstStep; i <= nums.length; i+= step) {
            if (step == 0) return false;

            if (step > nums.length) return true;
            try {
                step = nums[i];
            } catch(Exception e) {
                return true;
            }
        }
        return true;
            
        
    }
}

class CorrectSolution {
    public boolean canJump(int[] nums) {     
        int gas = 0;
        for (int n : nums) {
            if (gas < 0) {
                return false;
            } else if (n > gas) {
                gas = n;
            }

            gas -= 1;
        }

        return true;
    }
}
